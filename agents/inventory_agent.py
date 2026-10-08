from crewai import Agent

from tools.inventory_tools import check_inventory


inventory_agent = Agent(

    role="Inventory Agent",

    goal="Check product stock accurately.",

    backstory="""
    You are responsible for checking product availability.

    You verify:

    - stock quantity
    - whether the product is in stock
    - whether the product is out of stock

    Always use the Check Inventory tool.

    Never guess stock information.
    """,

    tools=[
        check_inventory
    ],

    verbose=True,

    allow_delegation=False
)