from crewai import Agent

from tools.refund_tools import (
    calculate_refund,
    process_mock_refund,
    get_refund_status
)


refund_agent = Agent(

    role="Refund Management Agent",

    goal="Process approved refunds accurately.",

    backstory="""
    You handle approved customer refunds.

    Verify:

    - order ID
    - refund amount
    - payment method
    - existing refund

    Never create duplicate refunds.

    The current system uses simulated refunds.

    No real money is transferred.

    Always use the refund tools.
    """,

    tools=[
        calculate_refund,
        process_mock_refund,
        get_refund_status
    ],

    verbose=True,

    allow_delegation=False
)