from langchain_core.messages import HumanMessage

from backend.agents.graph_agent import graph


test_cases = [

    {

        "question":

        "What is the return policy?",


        "ground_truth":

        "Customers may return products within 30 days of delivery."

    },


    {

        "question":

        "How long does shipping take?",


        "ground_truth":

        "Standard shipping takes 5-7 business days."

    }

]


score = 0


for tc in test_cases:


    state = {

        "messages": [

            HumanMessage(

                content=tc["question"]

            )

        ],

        "session_id":

        "eval"

    }


    response = graph.invoke(

        state

    )


    answer = response["messages"][-1].content


    print()

    print("=" * 30)

    print("Question:")

    print(tc["question"])



    print()

    print("Answer:")

    print(answer)



    print()

    print("Expected:")

    print(tc["ground_truth"])



    print()


    ####################################################
    # SCORING BLOCK
    ####################################################


    keywords = tc["ground_truth"].lower().split()


    matches = 0


    for word in keywords:


        if word in answer.lower():


            matches += 1



    similarity = matches / len(keywords)


    print(

        "Keyword Match Score:",

        round(

            similarity,

            2

        )

    )



    if similarity >= 0.7:


        score += 1


print()

print("=" * 30)

print("EVALUATION SCORE")

print("=" * 30)

print()


print(

    f"{score}/{len(test_cases)}"

)