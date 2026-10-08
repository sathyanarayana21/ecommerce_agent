from crewai.tools import tool

from data.mock_data import ORDERS, RETURNS


@tool("Check Return Eligibility")
def check_return_eligibility(order_id: str) -> str:
    """Check whether a delivered order is eligible for a return."""

    order = ORDERS.get(order_id)

    if not order:
        return f"Order {order_id} was not found."

    if order["status"] != "delivered":
        return "Return is not available because the order has not been delivered."

    delivery_date = order.get("delivery_date")

    if not delivery_date:
        return "Delivery date is unavailable."

    condition = order.get("condition", "good")

    return f"""
Order: {order_id}
Product: {order['product']}
Delivery Date: {delivery_date}
Product Condition: {condition}

Return Window: 7 days

Preliminary Return Eligibility:
Eligible for return verification.
"""


@tool("Create Return Request")
def create_return_request(order_id: str, reason: str) -> str:
    """Create a return request for an eligible order."""

    order = ORDERS.get(order_id)

    if not order:
        return f"Order {order_id} was not found."

    return_id = f"RET-{order_id}"

    RETURNS[return_id] = {
        "order_id": order_id,
        "product": order["product"],
        "reason": reason,
        "status": "return_requested"
    }

    return f"""
Return request created successfully.

Return ID: {return_id}
Order ID: {order_id}
Product: {order['product']}
Reason: {reason}
Status: return_requested
"""