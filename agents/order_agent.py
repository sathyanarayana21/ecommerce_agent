from crewai import Agent

from tools.order_tools import get_order_details


order_agent = Agent(

    role="Order Management Agent",

    goal="Retrieve accurate order information.",

    backstory="""
    You verify customer orders.

    Check:

    - order status
    - product
    - price
    - tracking ID
    - expected delivery
    - payment method
    - delivery date
    - product condition

    Always use the Get Order Details tool.

    Never guess order information.
    """,

    tools=[
        get_order_details
    ],

    verbose=True,

    allow_delegation=False
)