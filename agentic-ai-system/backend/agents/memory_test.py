from backend.agents.react_agent import run_agent


history = []


queries = [

    "What is your return policy?",

    "What about electronics?",

    "How long do refunds take?",

    "Do customized items qualify for return?"

]


for query in queries:


    result = run_agent(

        query,

        history

    )


    history = result["history"]


    print("\n")

    print("=" * 60)


    print("Question")

    print(query)



    print("\nAnswer")

    print(

        result["answer"]

    )



    print("\nHistory Size")


    print(

        len(history)

    )