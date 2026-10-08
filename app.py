import streamlit as st
from dotenv import load_dotenv

from crew import route_customer_request
from rag.policy_rag import build_policy_index


load_dotenv()


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="E-commerce AI Support",
    page_icon="🛒",
    layout="wide"
)


# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "rag_ready" not in st.session_state:
    st.session_state.rag_ready = False


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.title("🛒 E-commerce Agentic AI Support")

st.write(
    "Ask questions about orders, delivery, products, "
    "inventory, returns, refunds, and company policies."
)


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.header("System")

    st.success("CrewAI agents connected")

    if st.session_state.rag_ready:
        st.success("Policy RAG ready")
    else:
        st.warning("Policy RAG not initialized")

    st.divider()

    st.subheader("Example Questions")

    st.write("📦 Where is my order ORD1025?")

    st.write(
        "📱 What is the price of Apple iPhone 17?"
    )

    st.write(
        "📊 Is Apple iPhone 17 in stock?"
    )

    st.write(
        "🔄 I want to return order ORD3001."
    )

    st.write(
        "💰 What is the refund status for ORD3001?"
    )

    st.divider()

    if st.button(
        "🔄 Initialize / Rebuild Policy RAG",
        use_container_width=True
    ):

        with st.spinner("Building policy index..."):

            try:

                result = build_policy_index()

                st.session_state.rag_ready = True

                st.success(result)

            except Exception as e:

                st.error(
                    f"RAG initialization failed: {e}"
                )

    if st.button(
        "🗑️ Clear Chat",
        use_container_width=True
    ):

        st.session_state.messages = []

        st.rerun()


# ---------------------------------------------------------
# INITIALIZE RAG
# ---------------------------------------------------------

if not st.session_state.rag_ready:

    with st.spinner(
        "Initializing Policy RAG system..."
    ):

        try:

            result = build_policy_index()

            st.session_state.rag_ready = True

        except Exception as e:

            st.error(
                f"Could not initialize Policy RAG: {e}"
            )

            st.stop()


# ---------------------------------------------------------
# WELCOME MESSAGE
# ---------------------------------------------------------

if not st.session_state.messages:

    with st.chat_message("assistant"):

        st.markdown(
            """
            👋 Hello! I am your E-commerce AI Support Agent.

            I can help with:

            **Orders**  
            Check order information and status.

            **Delivery**  
            Track shipments and investigate delays.

            **Products**  
            Find product information and prices.

            **Inventory**  
            Check stock availability.

            **Returns**  
            Check eligibility and create return requests.

            **Refunds**  
            Calculate and process simulated refunds.

            **Policies**  
            Search company policies using RAG.
            """
        )


# ---------------------------------------------------------
# DISPLAY PREVIOUS CHAT
# ---------------------------------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# ---------------------------------------------------------
# CHAT INPUT
# ---------------------------------------------------------

customer_query = st.chat_input(
    "Ask your e-commerce question..."
)


if customer_query:

    # -----------------------------
    # Display user message
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "user",
            "content": customer_query
        }
    )

    with st.chat_message("user"):

        st.markdown(customer_query)


    # -----------------------------
    # Run CrewAI
    # -----------------------------

    with st.chat_message("assistant"):

        with st.spinner(
            "AI agents are processing your request..."
        ):

            try:

                result = route_customer_request(
                    customer_query
                )

                answer = str(result)

            except Exception as e:

                answer = (
                    "Sorry, I could not process your request.\n\n"
                    f"Error: `{e}`"
                )


        st.markdown(answer)


    # -----------------------------
    # Save assistant response
    # -----------------------------

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )