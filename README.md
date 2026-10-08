🛍️ E-Commerce Agentic AI Customer Support

Author: Sathyanarayana Janga

An AI-powered e-commerce customer support application built with Python, CrewAI, RAG, ChromaDB, Sentence Transformers, and Streamlit.

The project uses multiple specialized AI agents and tools to handle customer requests related to orders, delivery, products, inventory, returns, refunds, and company policies.

🚀 Project Overview

This project demonstrates how Agentic AI and Retrieval-Augmented Generation (RAG) can be combined to build an intelligent customer support system for an e-commerce application.

The application allows a customer to enter a question through a Streamlit chat interface. CrewAI agents then work with specialized tools and the policy RAG system to produce a final response.

The project is designed without FastAPI and without a traditional relational database.

✨ Features

🤖 Multi-agent customer support using CrewAI

🧠 RAG-based policy question answering

🔎 Semantic search using Sentence Transformers

⚡ ChromaDB vector store for policy retrieval

📦 Order information lookup

🚚 Delivery and shipment tracking

🛍️ Product information search

📊 Inventory availability checking

🔄 Return eligibility checking

📝 Return request creation

💰 Simulated refund processing

🛡️ Duplicate refund protection

💬 Interactive Streamlit chat interface

🔐 .env based API-key configuration

🚫 No FastAPI

🚫 No traditional relational database

🏗️ System Architecture

                         CUSTOMER
                            │
                            ▼
                     STREAMLIT UI
                            │
                            ▼
                 CUSTOMER SUPPORT AGENT
                            │
                            ▼
                    INTENT / REQUEST
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
          ▼                 ▼                 ▼
       ORDER            DELIVERY           PRODUCT
        AGENT             AGENT             AGENT
          │                 │                 │
          └────────────┬────┴─────────────────┘
                       │
                       ▼
                  INVENTORY AGENT
                       │
                       ▼
                   RETURN AGENT
                       │
                       ▼
                   POLICY AGENT
                       │
                       ▼
                      RAG
                       │
                       ▼
                   ChromaDB
                       │
                       ▼
              POLICY DOCUMENTS
                       │
                       ▼
                  REFUND AGENT
                       │
                       ▼
                RESOLUTION AGENT
                       │
                       ▼
                  FINAL ANSWER
                       │
                       ▼
                  STREAMLIT UI

🤖 AI Agents

The application contains the following agents:

Agent

Responsibility

Customer Support Agent

Understands the customer's request and intent

Order Agent

Retrieves and verifies order information

Delivery Agent

Investigates shipment and delivery status

Product Agent

Provides product information

Inventory Agent

Checks stock and availability

Return Agent

Checks return eligibility and creates return requests

Policy Agent

Retrieves company policies using RAG

Refund Agent

Calculates and processes simulated refunds

Resolution Agent

Produces the final customer-facing response

🧰 Tools

Order Tool

Retrieves order details using an order ID.

Delivery Tool

Retrieves shipment details using a tracking ID.

Product Tool

Searches product information such as brand, category, price, and description.

Inventory Tool

Checks stock quantity and product availability.

Return Tool

Checks return eligibility and creates a return request.

Policy Tool

Connects the CrewAI Policy Agent to the RAG policy search system.

Refund Tool

Calculates refunds, processes simulated refunds, checks refund status, and prevents duplicate refunds.

🧠 RAG Architecture

Company policies are stored as text documents rather than as policy information inside a Python dictionary.

rag/
└── policy_documents/
    ├── return_policy.txt
    ├── refund_policy.txt
    ├── cancellation_policy.txt
    └── delivery_policy.txt

The policy retrieval flow is:

Customer Question
       ↓
Policy Agent
       ↓
Policy Search Tool
       ↓
Sentence Transformer
       ↓
Question Embedding
       ↓
ChromaDB Similarity Search
       ↓
Relevant Policy Documents
       ↓
Policy Agent
       ↓
Final Response

This allows the Policy Agent to answer using the information retrieved from the policy knowledge base.

📁 Project Structure

ecommerce_agent/
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── main.py
├── crew.py
│
├── data/
│   ├── __init__.py
│   └── mock_data.py
│
├── rag/
│   ├── __init__.py
│   ├── policy_rag.py
│   └── policy_documents/
│       ├── return_policy.txt
│       ├── refund_policy.txt
│       ├── cancellation_policy.txt
│       └── delivery_policy.txt
│
├── tools/
│   ├── __init__.py
│   ├── product_tools.py
│   ├── order_tools.py
│   ├── delivery_tools.py
│   ├── inventory_tools.py
│   ├── return_tools.py
│   ├── policy_tools.py
│   └── refund_tools.py
│
└── agents/
    ├── __init__.py
    ├── customer_support.py
    ├── order_agent.py
    ├── delivery_agent.py
    ├── product_agent.py
    ├── inventory_agent.py
    ├── return_agent.py
    ├── policy_agent.py
    ├── refund_agent.py
    └── resolution_agent.py

🛠️ Technologies Used

Python 3.11

CrewAI – multi-agent orchestration

Streamlit – interactive web interface

ChromaDB – vector store for policy retrieval

Sentence Transformers – text embeddings

PyTorch / TorchVision – machine-learning dependencies used by the embedding stack

python-dotenv – environment variable management

OpenAI API – language model access

⚙️ Installation

1. Clone the repository

git clone <your-github-repository-url>
cd ecommerce_agent

2. Create a virtual environment

python -m venv .venv

3. Activate the virtual environment

Windows PowerShell:

.\.venv\Scripts\Activate.ps1

4. Install dependencies

pip install -r requirements.txt

🔑 Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here

Do not upload your real API key to GitHub.

A safe template can be kept in .env.example:

OPENAI_API_KEY=your_api_key_here

▶️ Run the Command-Line Application

python main.py

The command-line version allows you to enter a customer question directly in the terminal.

🌐 Run the Streamlit Application

Start the web application with:

python -m streamlit run app.py

The Streamlit application provides a colorful customer-support chat interface where users can enter e-commerce questions.

💬 Example Questions

Order

What is the status of order ORD3001?

Delivery

Where is my order ORD1025?

Product

What is the price of Apple iPhone 17?

Inventory

Is Apple iPhone 17 in stock?

Return

I want to return order ORD3001 because it arrived damaged.

Refund

What is the refund status for ORD3001?

Return + Refund

My order ORD3001 arrived damaged. I want to return it and get a refund.

💰 Refund Handling

Refunds in this project are simulated refunds for demonstration purposes.

No real money is transferred.

The refund tool also checks whether a refund already exists for an order before creating another one.

📚 Sample Business Data

The application uses mock e-commerce data stored in:

data/mock_data.py

This includes sample information for:

Orders

Products

Inventory

Shipments

Returns

Refunds

This keeps the project simple for learning and demonstration purposes.

🔒 GitHub Safety

The following files and folders should not be committed to GitHub:

.env
.venv/
__pycache__/
rag/chroma_db/
.idea/
.vscode/

Use .gitignore to keep API keys, virtual environments, cached files, IDE configuration, and generated vector-store data out of the repository.

🎯 Project Objective

The objective of this project is to demonstrate how Agentic AI + RAG + Tool Calling can be used to build an intelligent e-commerce customer-support application.

The system combines:

Multi-Agent AI
        +
Tool Calling
        +
RAG
        +
Vector Search
        +
Streamlit

to create an interactive AI customer-support experience.

🔮 Future Enhancements

Possible future improvements include:

Persistent conversation memory

Better intent routing

Authentication and user accounts

Real e-commerce APIs

Real order-management integration

Real payment/refund integration

Admin dashboard

Deployment to Streamlit Community Cloud

Monitoring and agent-performance analytics

👨‍💻 Author

Sathyanarayana Janga

E-Commerce Agentic AI Customer Support

Built as a learning and demonstration project using Python, CrewAI, RAG, ChromaDB, Sentence Transformers, and Streamlit.
