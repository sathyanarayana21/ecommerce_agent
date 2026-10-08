from crewai.tools import tool

from data.mock_data import ORDERS, REFUNDS


@tool("Calculate Refund")
def calculate_refund(order_id: str) -> str:
    """Calculate the refund amount for an order."""

    order = ORDERS.get(order_id)

    if not order:
        return f"Order {order_id} was not found."

    amount = order["price"]

    return f"""
Order ID: {order_id}
Product: {order['product']}
Original Price: ₹{amount}
Approved Refund Amount: ₹{amount}
"""


@tool("Process Mock Refund")
def process_mock_refund(order_id: str) -> str:
    """Process a simulated refund and prevent duplicate refunds."""

    if order_id in REFUNDS:
        return f"""
Refund already exists for order {order_id}.

Refund ID: {REFUNDS[order_id]['refund_id']}
Status: {REFUNDS[order_id]['status']}
"""

    order = ORDERS.get(order_id)

    if not order:
        return f"Order {order_id} was not found."

    refund_id = f"REF-{order_id}"

    REFUNDS[order_id] = {
        "refund_id": refund_id,
        "amount": order["price"],
        "status": "refund_initiated",
        "payment_method": order["payment_method"]
    }

    return f"""
Mock refund initiated.

Refund ID: {refund_id}
Order ID: {order_id}
Amount: ₹{order['price']}
Payment Method: {order['payment_method']}
Status: refund_initiated

IMPORTANT:
This is a simulated refund.
No real money was transferred.
"""


@tool("Get Refund Status")
def get_refund_status(order_id: str) -> str:
    """Check the refund status for an order."""

    refund = REFUNDS.get(order_id)

    if not refund:
        return f"No refund found for order {order_id}."

    return f"""
Order ID: {order_id}
Refund ID: {refund['refund_id']}
Amount: ₹{refund['amount']}
Payment Method: {refund['payment_method']}
Status: {refund['status']}
"""