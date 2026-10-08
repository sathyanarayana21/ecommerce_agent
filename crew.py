from crewai import Crew, Task, Process

from agents.customer_support import customer_support_agent
from agents.order_agent import order_agent
from agents.delivery_agent import delivery_agent
from agents.product_agent import product_agent
from agents.inventory_agent import inventory_agent
from agents.return_agent import return_agent
from agents.policy_agent import policy_agent
from agents.refund_agent import refund_agent
from agents.resolution_agent import resolution_agent


def create_router_crew(customer_query: str):

    router_task = Task(
        description=f"""
        Analyze the customer request and select the PRIMARY intent.

        Customer request:
        {customer_query}

        Choose exactly ONE of:

        ORDER
        DELIVERY
        PRODUCT
        INVENTORY
        RETURN
        REFUND
        RETURN_REFUND
        GENERAL

        Rules:

        DELIVERY:
        Tracking, shipment, package location, delay,
        estimated delivery or delivery problem.

        PRODUCT:
        Product name, brand, category, price or description.

        INVENTORY:
        Stock or availability.

        RETURN:
        Customer wants to return a product.

        REFUND:
        Customer asks about refund status, refund amount,
        or an already-created refund.

        RETURN_REFUND:
        Customer wants both a return and a refund.

        ORDER:
        General order information or order status.

        GENERAL:
        Anything else.

        Return ONLY the route name.
        """,

        expected_output="""
        Exactly one route name.
        """,

        agent=customer_support_agent
    )

    crew = Crew(
        agents=[customer_support_agent],
        tasks=[router_task],
        process=Process.sequential,
        verbose=True
    )

    return crew, router_task


def create_order_crew(customer_query: str):

    order_task = Task(
        description=f"""
        Answer the customer's order question.

        Customer request:
        {customer_query}

        Identify the order ID.

        Use the Get Order Details tool.

        Never invent information.
        """,

        expected_output="""
        Verified order information and a helpful answer.
        """,

        agent=order_agent
    )

    resolution_task = Task(
        description="""
        Prepare a concise customer-facing response
        using the verified order information.

        Never invent information.
        """,

        expected_output="""
        Professional customer response.
        """,

        agent=resolution_agent,
        context=[order_task]
    )

    return Crew(
        agents=[order_agent, resolution_agent],
        tasks=[order_task, resolution_task],
        process=Process.sequential,
        verbose=True
    )


def create_delivery_crew(customer_query: str):

    order_task = Task(
        description=f"""
        Identify the order ID from the customer's request.

        Customer request:
        {customer_query}

        Use the Get Order Details tool.

        Retrieve the tracking ID.

        Never invent information.
        """,

        expected_output="""
        Verified order information including the tracking ID.
        """,

        agent=order_agent
    )

    delivery_task = Task(
        description="""
        Use the verified tracking ID from the previous task.

        Use the Get Shipment Details tool.

        Explain:
        - shipment status
        - current location
        - reason for delay
        - updated estimated delivery

        Never invent shipment information.
        """,

        expected_output="""
        Verified shipment information.
        """,

        agent=delivery_agent,
        context=[order_task]
    )

    resolution_task = Task(
        description="""
        Prepare the final customer-facing delivery response.

        Use only verified information.

        Never invent a delivery date.
        """,

        expected_output="""
        Professional delivery response.
        """,

        agent=resolution_agent,
        context=[order_task, delivery_task]
    )

    return Crew(
        agents=[
            order_agent,
            delivery_agent,
            resolution_agent
        ],

        tasks=[
            order_task,
            delivery_task,
            resolution_task
        ],

        process=Process.sequential,
        verbose=True
    )


def create_product_crew(customer_query: str):

    product_task = Task(
        description=f"""
        Answer the customer's product question.

        Customer request:
        {customer_query}

        Use the Search Product tool.

        Never invent product information.
        """,

        expected_output="""
        Verified product information.
        """,

        agent=product_agent
    )

    resolution_task = Task(
        description="""
        Prepare the final customer response
        using the verified product information.
        """,

        expected_output="""
        Professional product response.
        """,

        agent=resolution_agent,
        context=[product_task]
    )

    return Crew(
        agents=[product_agent, resolution_agent],
        tasks=[product_task, resolution_task],
        process=Process.sequential,
        verbose=True
    )


def create_inventory_crew(customer_query: str):

    inventory_task = Task(
        description=f"""
        Answer the customer's inventory question.

        Customer request:
        {customer_query}

        Use the Check Inventory tool.

        Never guess stock.
        """,

        expected_output="""
        Verified inventory information.
        """,

        agent=inventory_agent
    )

    resolution_task = Task(
        description="""
        Prepare the final customer response
        using the verified inventory information.
        """,

        expected_output="""
        Professional inventory response.
        """,

        agent=resolution_agent,
        context=[inventory_task]
    )

    return Crew(
        agents=[inventory_agent, resolution_agent],
        tasks=[inventory_task, resolution_task],
        process=Process.sequential,
        verbose=True
    )


def create_return_crew(customer_query: str):

    return_task = Task(
        description=f"""
        Handle the customer's return request.

        Customer request:
        {customer_query}

        Identify the order ID.

        Use:
        1. Check Return Eligibility
        2. Create Return Request if eligible

        Do not process a refund.
        """,

        expected_output="""
        Return eligibility and return request information.
        """,

        agent=return_agent
    )

    policy_task = Task(
        description=f"""
        Determine the correct return policy.

        Customer request:
        {customer_query}

        MUST use the Search E-commerce Policies tool.

        Use only information retrieved from RAG.
        Never invent policy.
        """,

        expected_output="""
        Applicable return policy and decision.
        """,

        agent=policy_agent,
        context=[return_task]
    )

    resolution_task = Task(
        description="""
        Prepare the final customer-facing response.

        Include:
        - return decision
        - policy result
        - return ID if available
        - next steps

        Do not mention a refund unless
        refund information exists.
        """,

        expected_output="""
        Professional return response.
        """,

        agent=resolution_agent,
        context=[return_task, policy_task]
    )

    return Crew(
        agents=[
            return_agent,
            policy_agent,
            resolution_agent
        ],

        tasks=[
            return_task,
            policy_task,
            resolution_task
        ],

        process=Process.sequential,
        verbose=True
    )


def create_refund_crew(customer_query: str):

    policy_task = Task(
        description=f"""
        Determine the applicable refund policy.

        Customer request:
        {customer_query}

        MUST use the Search E-commerce Policies tool.

        Use only retrieved policy information.
        Never invent policy.
        """,

        expected_output="""
        Applicable refund policy.
        """,

        agent=policy_agent
    )

    refund_task = Task(
        description=f"""
        Handle the refund request.

        Customer request:
        {customer_query}

        Review the policy.

        Use the refund tools.

        Check for an existing refund before
        creating a new refund.

        This is a simulated refund.
        No real money is transferred.
        """,

        expected_output="""
        Refund status, refund ID, amount,
        payment method and simulation status.
        """,

        agent=refund_agent,
        context=[policy_task]
    )

    resolution_task = Task(
        description="""
        Prepare the final customer response.

        Include:
        - refund status
        - refund ID if available
        - amount
        - payment method
        - simulated refund notice
        """,

        expected_output="""
        Professional refund response.
        """,

        agent=resolution_agent,
        context=[policy_task, refund_task]
    )

    return Crew(
        agents=[
            policy_agent,
            refund_agent,
            resolution_agent
        ],

        tasks=[
            policy_task,
            refund_task,
            resolution_task
        ],

        process=Process.sequential,
        verbose=True
    )


def create_return_refund_crew(customer_query: str):

    return_task = Task(
        description=f"""
        Handle the customer's return request.

        Customer request:
        {customer_query}

        Identify the order ID.

        Check return eligibility.

        If eligible, create the return request.

        Do not process the refund.
        """,

        expected_output="""
        Verified return eligibility and return request.
        """,

        agent=return_agent
    )

    policy_task = Task(
        description=f"""
        Determine the applicable return and refund policies.

        Customer request:
        {customer_query}

        MUST use the Search E-commerce Policies tool.

        Use only information retrieved from RAG.
        Never invent policy.
        """,

        expected_output="""
        Applicable return and refund policy information.
        """,

        agent=policy_agent,
        context=[return_task]
    )

    refund_task = Task(
        description="""
        Review the return result and policy.

        Process the refund only when the previous
        information supports the refund.

        Use the refund tools.

        Prevent duplicate refunds.

        This is a simulated refund.
        No real money is transferred.
        """,

        expected_output="""
        Refund decision and refund information.
        """,

        agent=refund_agent,
        context=[return_task, policy_task]
    )

    resolution_task = Task(
        description="""
        Prepare the final customer-facing response.

        Include:
        - order information when available
        - return result
        - policy result
        - return ID
        - refund ID when available
        - refund amount
        - payment method
        - next steps

        Clearly state that the refund is simulated.
        Never invent information.
        """,

        expected_output="""
        Professional final response.
        """,

        agent=resolution_agent,
        context=[
            return_task,
            policy_task,
            refund_task
        ]
    )

    return Crew(
        agents=[
            return_agent,
            policy_agent,
            refund_agent,
            resolution_agent
        ],

        tasks=[
            return_task,
            policy_task,
            refund_task,
            resolution_task
        ],

        process=Process.sequential,
        verbose=True
    )


def route_customer_request(customer_query: str):

    router_crew, router_task = create_router_crew(
        customer_query
    )

    router_crew.kickoff()

    route = router_task.output.raw.strip().upper()

    print()
    print("=" * 80)
    print("ROUTING DECISION")
    print("=" * 80)
    print(route)

    if "RETURN_REFUND" in route:
        crew = create_return_refund_crew(customer_query)

    elif "DELIVERY" in route:
        crew = create_delivery_crew(customer_query)

    elif "PRODUCT" in route:
        crew = create_product_crew(customer_query)

    elif "INVENTORY" in route:
        crew = create_inventory_crew(customer_query)

    elif "RETURN" in route:
        crew = create_return_crew(customer_query)

    elif "REFUND" in route:
        crew = create_refund_crew(customer_query)

    elif "ORDER" in route:
        crew = create_order_crew(customer_query)

    else:
        crew = create_order_crew(customer_query)

    return crew.kickoff()