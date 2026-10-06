import traceback
import json
import asyncio
import os

from dotenv import load_dotenv

load_dotenv()

print("\n===== LANGFUSE VARIABLES =====")
print("PUBLIC =", os.getenv("LANGFUSE_PUBLIC_KEY"))
print("SECRET =", os.getenv("LANGFUSE_SECRET_KEY"))
print("HOST =", os.getenv("LANGFUSE_HOST"))
print("==============================\n")

from fastapi import (
    APIRouter,
    HTTPException,
    WebSocket,
    Request
)

from langchain_core.messages import HumanMessage

from langfuse import Langfuse

from backend.api.models import ChatRequest, ChatResponse
from backend.agents.graph_agent import graph as agent_graph

from backend.api.guardrails import (
    validate_input,
    validate_output
)

from backend.api.output_filter import filter_output

from backend.api.limiter import limiter

from backend.core.logging import logger

router = APIRouter()

####################################################
# Langfuse Client
####################################################

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST"),
)
print("Langfuse object:", langfuse)
print("Langfuse type:", type(langfuse))
print("Has trace:", hasattr(langfuse, "trace"))
print("Methods:", dir(langfuse))

####################################################
# Chat Endpoint
####################################################

@router.post(
    "/chat",
    response_model=ChatResponse
)
@limiter.limit("10/minute")
async def chat(
    request: Request,
    body: ChatRequest
):

    try:

        ####################################################
        # Input Validation
        ####################################################

        body.message = validate_input(body.message)
        logger.info(
            "Agent invoked",
            extra={
                "session_id": body.session_id
            }
        )

        ####################################################
        # Create Langfuse Trace
        ####################################################

        # trace = langfuse.trace(
        #     name="customer-support-chat",
        #     session_id=body.session_id
        # )

        ####################################################
        # Invoke Agent
        ####################################################

        result = await agent_graph.ainvoke(
            {
                "messages": [
                    HumanMessage(content=body.message)
                ],
                "session_id": body.session_id,
            }
        )

        last = result["messages"][-1]

        tool_calls = sum(
            1
            for m in result["messages"]
            if hasattr(m, "tool_calls") and m.tool_calls
        )

        ####################################################
        # Token Usage
        ####################################################

        input_tokens = result.get("input_tokens", 0)
        output_tokens = result.get("output_tokens", 0)
        total_tokens = result.get("total_tokens", 0)

        logger.info(
            "Agent completed",
            extra={
                "session_id": body.session_id,
                "tokens": total_tokens
            }
        )

        ####################################################
        # Update Langfuse Trace
        ####################################################

        # trace.update(
    #     input=body.message,
    #     output=last.content,
    #     metadata={
    #         "session_id": body.session_id,
    #         "tool_calls": tool_calls,
    #     },
    # )

        ####################################################
        # Log LLM Generation
        ####################################################

        #trace.generation(
        #    name="llm-response",
         #   input=body.message,
          #  output=last.content,
           # usage={
            #    "input": input_tokens,
             #   "output": output_tokens,
              #  "total": total_tokens,
          #  },
        #)

        ####################################################
        # Flush Trace
        ####################################################

        #langfuse.flush()

        ####################################################
        # Output Guardrails
        ####################################################

        answer = validate_output(last.content)

        answer = filter_output(answer)

        ####################################################
        # Response
        ####################################################

        return ChatResponse(
            answer=answer,
            session_id=body.session_id,
            tool_calls_made=tool_calls,
            sources=[]
        )

    except HTTPException:
        raise

    except Exception as e:

        traceback.print_exc()   # <-- ADD THIS LINE

        logger.exception(
            "Chat endpoint failed",
            extra={
                "session_id": body.session_id
            }
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


####################################################
# WebSocket Endpoint (Uses LangGraph + RAG)
####################################################

@router.websocket("/ws/{session_id}")
async def websocket_chat(
    websocket: WebSocket,
    session_id: str
):

    await websocket.accept()

    try:

        while True:

            user_msg = await websocket.receive_text()

            print(f"\nReceived message: {user_msg}")

            ####################################################
            # Input Validation
            ####################################################

            user_msg = validate_input(user_msg)

            ####################################################
            # Invoke LangGraph (Uses RAG)
            ####################################################

            result = await agent_graph.ainvoke(
                {
                    "messages": [
                        HumanMessage(content=user_msg)
                    ],
                    "session_id": session_id,
                }
            )

            last = result["messages"][-1]

            ####################################################
            # Filter Output
            ####################################################

            answer = validate_output(last.content)
            answer = filter_output(answer)

            ####################################################
            # Stream Answer
            ####################################################

            for word in answer.split():

                await websocket.send_text(word + " ")

                await asyncio.sleep(0.02)

            ####################################################
            # Done
            ####################################################

            await websocket.send_text("[DONE]")

    except Exception as e:

        traceback.print_exc()

        print("WebSocket Error:", e)

        try:
            await websocket.close()
        except Exception:
            pass