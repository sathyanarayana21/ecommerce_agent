from crewai.tools import tool

from data.mock_data import ORDERS


@tool("Get Order Details")
def get_order_details(order_id: str) -> str:
    """Retrieve complete order information using the order ID."""

    order = ORDERS.get(order_id)

    if not order:
        return f"Order {order_id} was not found."

    return f"""
Order ID: {order_id}
Customer: {order['customer']}
Product: {order['product']}
Category: {order['category']}
Price: ₹{order['price']}
Order Date: {order['order_date']}
Expected Delivery: {order['expected_delivery']}
Status: {order['status']}
Tracking ID: {order['tracking_id']}
Payment Method: {order['payment_method']}
Delivery Date: {order.get('delivery_date', 'N/A')}
Condition: {order.get('condition', 'N/A')}
"""