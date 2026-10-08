from crewai.tools import tool

from data.mock_data import PRODUCTS


@tool("Search Product")
def search_product(product_name: str) -> str:
    """Search for product information using the product name."""

    product = PRODUCTS.get(product_name)

    if not product:
        return f"Product '{product_name}' was not found."

    return f"""
Product: {product_name}
Brand: {product['brand']}
Category: {product['category']}
Price: ₹{product['price']}
Description: {product['description']}
"""