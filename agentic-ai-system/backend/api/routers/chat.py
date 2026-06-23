from fastapi import WebSocket
from langchain_ollama import ChatOllama
from fastapi import APIRouter, HTTPException
from langchain_core.messages import HumanMessage

from backend.api.models import ChatRequest, ChatResponse
from backend.agents.graph_agent import graph as agent_graph


router = APIRouter()


@router.post(
    "/chat",
    response_model=ChatResponse
)
async def chat(request: ChatRequest):

    try:

        result = agent_graph.invoke(

            {
                "messages": [
                    HumanMessage(
                        content=request.message
                    )
                ],

                "session_id": request.session_id
            }

        )

        last = result["messages"][-1]

        tool_calls = sum(

            1

            for m in result["messages"]

            if hasattr(m, "tool_calls")
            and m.tool_calls

        )

        return ChatResponse(

            answer=last.content,

            session_id=request.session_id,

            tool_calls_made=tool_calls,

            sources=[]

        )

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )
####################################################
# WebSocket Streaming Endpoint
####################################################

@router.websocket("/ws/{session_id}")
async def websocket_chat(
        websocket: WebSocket,
        session_id: str
):

    await websocket.accept()


    llm_stream = ChatOllama(

        model="llama3.1:8b",

        streaming=True

    )


    try:

        while True:


            user_msg = await websocket.receive_text()


            async for chunk in llm_stream.astream(


                    user_msg

            ):


                if chunk.content:


                    await websocket.send_text(

                        chunk.content

                    )


            await websocket.send_text(


                "[DONE]"

            )


    except Exception:


        await websocket.close()
