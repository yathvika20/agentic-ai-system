from langchain_core.tools import tool
from pydantic import BaseModel, Field

from backend.rag.retriever import KnowledgeBaseRetriever


####################################################
# Create retriever once when the application starts
####################################################

_retriever = KnowledgeBaseRetriever()


####################################################
# Tool Schemas
####################################################

class OrderStatusInput(BaseModel):
    order_id: str | int = Field(
        description="Customer order ID"
    )


####################################################
# Knowledge Base Tool
####################################################

@tool
def search_knowledge_base(query: str) -> str:
    """
    Use ONLY for:

    - FAQs
    - Return policy
    - Refund policy
    - Product information
    - Shipping policy
    - Warranty

    Do NOT use this tool for order tracking.
    """

    results = _retriever.retrieve(query)

    if not results:
        return "No relevant information found in the knowledge base."

    context = "\n---\n".join(results)

    return (
        "Relevant information from knowledge base:\n\n"
        f"{context}"
    )


####################################################
# Order Status Tool
####################################################

@tool(args_schema=OrderStatusInput)
def check_order_status(order_id: str | int) -> str:
    """
    Use this tool ONLY when the user provides an order ID
    and asks about:

    - Order status
    - Order tracking
    - Shipment
    - Delivery
    - Where is my order

    Input:
        order_id

    Returns:
        Current shipping status.
    """

    # Convert numeric order IDs to strings
    # so both 1001 and "1001" are handled correctly.
    order_id = str(order_id)

    return (
        f"Order {order_id} has been shipped "
        "and will arrive tomorrow."
    )


####################################################
# Escalation Tool
####################################################

@tool
def escalate_to_human(issue: str) -> str:
    """
    Escalate unresolved issues to a human support agent.
    """

    return (
        f"Issue escalated to human support: "
        f"{issue}"
    )


####################################################
# Test
####################################################

if __name__ == "__main__":

    result = search_knowledge_base.invoke(
        {
            "query": "What is the return policy?"
        }
    )

    print(result)