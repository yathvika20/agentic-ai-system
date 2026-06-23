from backend.agents.graph_agent import graph
from langchain_core.messages import HumanMessage

config = {
    "configurable": {
        "thread_id": "test-session-1"
    }
}

questions = [
    "What is your return policy?",
    "And how long does shipping take?",
    "My order #777 has not arrived"
]

for question in questions:

    result = graph.invoke(

        {
            "messages": [HumanMessage(content=question)],
            "session_id": "test-1"
        },

        config=config

    )

    last_msg = result["messages"][-1]

    print(f"\nQ: {question}")
    print(f"A: {last_msg.content[:200]}")