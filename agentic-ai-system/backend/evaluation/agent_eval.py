import json

from langchain_core.messages import HumanMessage

from backend.agents.graph_agent import graph


with open(

        "backend/evaluation/test_cases.json",

        "r",

        encoding="utf-8"

) as f:

    tests = json.load(f)


passed = 0


for tc in tests:


    state = {

        "messages": [

            HumanMessage(

                content=tc["input"]

            )

        ],

        "session_id":

        "eval"

    }


    result = graph.invoke(

        state

    )


    answer = result["messages"][-1].content


    success = tc["expected_contains"].lower(

    ) in answer.lower()


    print()

    print("=" * 40)

    print(

        "Question:",

        tc["input"]

    )


    print()

    print(

        "Expected:",

        tc["expected_contains"]

    )


    print()

    print(

        "Answer:",

        answer

    )


    print()


    if success:


        print(

            "PASS"

        )


        passed += 1


    else:


        print(

            "FAIL"

        )


print()

print("=" * 40)

print(

    "FINAL SCORE"

)

print(

    f"{passed}/{len(tests)}"

)