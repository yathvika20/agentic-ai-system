from backend.agents.react_agent import run_agent


# Existing tests
test_cases = [

    "What is your return policy?",

    "Where is my order 9999?",

    "I want a refund for a broken product"

]


for query in test_cases:

    print("\n")
    print("=" * 50)

    print("Question")
    print(query)

    result = run_agent(query)

    print("\nAnswer")
    print(result["answer"])



# ==========================================================
# Task 7
# ==========================================================

print("\n")
print("=" * 50)
print("=== Multi-turn memory test ===")


run_agent(

    "Hi, my name is Manigandan",

    "session_001"

)


result = run_agent(

    "What did I just tell you my name was?",

    "session_001"

)


print("\nShould remember name:")

print(

    result["answer"]

)