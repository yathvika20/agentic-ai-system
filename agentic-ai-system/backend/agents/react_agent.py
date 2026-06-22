from langchain_ollama import ChatOllama

from langchain_core.messages import (
    HumanMessage,
    SystemMessage,
    ToolMessage
)

from backend.agents.tools import (
    search_knowledge_base,
    check_order_status,
    escalate_to_human
)

from backend.agents.prompts import AGENT_SYSTEM
from backend.agents.memory import memory


tools = [
    search_knowledge_base,
    check_order_status,
    escalate_to_human
]

tool_map = {
    t.name: t
    for t in tools
}


def run_agent(
        user_input: str,
        session_id: str = "default"
) -> dict:

    llm = ChatOllama(
        model="llama3.1:8b"
    ).bind_tools(tools)

    history = memory.get_history(session_id)

    messages = [

        SystemMessage(
            content=AGENT_SYSTEM
        )

    ] + history + [

        HumanMessage(
            content=user_input
        )

    ]

    new_messages = []

    for i in range(5):

        response = llm.invoke(messages)

        messages.append(response)

        new_messages.append(response)

        if not response.tool_calls:

            memory.add_messages(

                session_id,

                [

                    HumanMessage(

                        content=user_input

                    )

                ]

                +

                new_messages

            )

            return {

                "answer": response.content,

                "session_id": session_id

            }

        for tc in response.tool_calls:

            result = tool_map[

                tc["name"]

            ].invoke(

                tc["args"]

            )

            tm = ToolMessage(

                content=str(result),

                tool_call_id=tc["id"]

            )

            messages.append(tm)

            new_messages.append(tm)

    memory.add_messages(

        session_id,

        [

            HumanMessage(

                content=user_input

            )

        ]

        +

        new_messages

    )

    return {

        "answer":

        "Maximum iterations reached.",

        "session_id":

        session_id

    }