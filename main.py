from dotenv import load_dotenv

from crew import route_customer_request
from rag.policy_rag import build_policy_index


load_dotenv()


def main():

    print("=" * 80)
    print("       E-COMMERCE AGENTIC AI CUSTOMER SUPPORT")
    print("=" * 80)

    print()
    print("Building Policy RAG index...")

    result = build_policy_index()

    print(result)

    print()
    print("System ready!")
    print()
    print("Type 'exit' to stop the program.")

    while True:

        print()

        customer_query = input(
            "Enter your question: "
        ).strip()

        if customer_query.lower() == "exit":
            print()
            print("Thank you for using the E-commerce Agent.")
            break

        if not customer_query:
            print("Please enter a question.")
            continue

        print()
        print("=" * 80)
        print("PROCESSING REQUEST")
        print("=" * 80)

        try:

            result = route_customer_request(
                customer_query
            )

            print()
            print("=" * 80)
            print("FINAL CUSTOMER RESPONSE")
            print("=" * 80)

            print(result)

        except Exception as e:

            print()
            print("=" * 80)
            print("ERROR")
            print("=" * 80)

            print(e)


if __name__ == "__main__":
    main()