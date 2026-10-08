from crewai.tools import tool

from data.mock_data import INVENTORY


@tool("Check Inventory")
def check_inventory(product_name: str) -> str:
    """Check the current stock quantity and availability of a product."""

    product = INVENTORY.get(product_name)

    if not product:
        return f"Inventory information not available for '{product_name}'."

    stock = product["stock"]

    if stock > 0:
        availability = "In Stock"
    else:
        availability = "Out of Stock"

    return f"""
Product: {product_name}
Stock Quantity: {stock}
Availability: {availability}
"""