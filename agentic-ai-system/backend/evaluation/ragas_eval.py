from datasets import Dataset

from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
)

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama

from backend.agents.graph_agent import graph
from backend.rag.retriever import KnowledgeBaseRetriever


####################################################
# Evaluation LLM
####################################################

evaluator_llm = ChatOllama(
    model="llama3.1:8b"
)


####################################################
# Test Questions
####################################################

test_cases = [
    {
        "question": "What is the return policy?",
        "ground_truth": "Customers may return products within 30 days of delivery."
    },
    {
        "question": "How long does shipping take?",
        "ground_truth": "Standard shipping takes 5-7 business days."
    }
]


####################################################
# Retriever
####################################################

retriever = KnowledgeBaseRetriever()

results = []


####################################################
# Generate Answers
####################################################

print("\nGenerating responses...\n")

for tc in test_cases:

    # Retrieve documents
    retrieved_docs = retriever.retrieve(tc["question"])

    if isinstance(retrieved_docs, list):
        retrieved_contexts = [str(doc) for doc in retrieved_docs]
    else:
        retrieved_contexts = [str(retrieved_docs)]

    # Run Agent
    state = {
        "messages": [
            HumanMessage(content=tc["question"])
        ],
        "session_id": "ragas_eval"
    }

    response = graph.invoke(state)

    answer = response["messages"][-1].content

    results.append(
        {
            "user_input": tc["question"],
            "retrieved_contexts": retrieved_contexts,
            "response": answer,
            "reference": tc["ground_truth"],
        }
    )


####################################################
# Create Dataset
####################################################

dataset = Dataset.from_list(results)

print("\n==============================")
print("DATASET")
print("==============================\n")

print(dataset)

print("\nFirst Sample:\n")
print(dataset[0])


####################################################
# Run RAGAS
####################################################

print("\n==============================")
print("STARTING RAGAS EVALUATION")
print("==============================\n")

scores = evaluate(
    dataset=dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
    ],
    llm=evaluator_llm,
)


####################################################
# Print Scores
####################################################

print("\n==============================")
print("RAGAS SCORES")
print("==============================\n")

print(scores)

try:
    print("\nAs Dictionary:\n")
    print(scores.to_pandas())
except Exception:
    pass