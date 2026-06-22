from langchain_core.tools import tool
from backend.rag.retriever import KnowledgeBaseRetriever


# Create retriever once when the application starts
_retriever = KnowledgeBaseRetriever()


@tool
def search_knowledge_base(query: str) -> str:
    """
    Search the product knowledge base for information.
    Use for product questions, policies, FAQs.
    """

    results = _retriever.retrieve(query)

    if not results:
        return "No relevant information found in the knowledge base."

    context = "\n---\n".join(results)

    return f"Relevant information from knowledge base:\n\n{context}"


@tool
def check_order_status(order_id: str) -> str:
    """
    Check the status of an order.
    """

    return f"Order {order_id} has been shipped and will arrive tomorrow."


@tool
def escalate_to_human(issue: str) -> str:
    """
    Escalate unresolved issues to a human support agent.
    """

    return f"Issue escalated to human support: {issue}"


if __name__ == "__main__":

    result = search_knowledge_base.invoke(

        {"query": "What is the return policy?"}

    )

    print(result)

@tool
def check_order_status(order_id: str) -> str:
    """
    Check order status.
    """

    return (
        f"Order {order_id} has been shipped "
        "and will arrive tomorrow."
    )


@tool
def escalate_to_human(issue: str) -> str:
    """
    Escalate unresolved issues.
    """

    return (
        f"Issue escalated to human support: "
        f"{issue}"
    )