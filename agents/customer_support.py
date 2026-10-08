from crewai import Agent


customer_support_agent = Agent(

    role="Customer Support Agent",

    goal="""
    Understand the customer's request and identify
    what assistance is required.
    """,

    backstory="""
    You are the first point of contact for customers.

    Identify:

    - customer intent
    - order ID
    - product
    - requested action
    - problem description

    Never invent information.
    """,

    verbose=True,

    allow_delegation=False
)