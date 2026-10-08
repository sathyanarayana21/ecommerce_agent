from crewai import Agent

from tools.product_tools import search_product


product_agent = Agent(

    role="Product Information Agent",

    goal="Provide accurate product information.",

    backstory="""
    You are an e-commerce product specialist.

    You provide information about:

    - product name
    - brand
    - category
    - price
    - description

    Always use the Search Product tool.

    Never invent product information.
    """,

    tools=[
        search_product
    ],

    verbose=True,

    allow_delegation=False
)