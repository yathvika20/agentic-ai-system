from backend.agents.react_agent import run_agent


session = "user123"


queries = [

    "What is your return policy?",

    "What about electronics?",

    "How long do refunds take?"

]


for q in queries:


    result = run_agent(

        q,

        session

    )


    print("\n")

    print("=" * 50)


    print("Question")

    print(q)


    print("\nAnswer")

    print(

        result["answer"]

    )