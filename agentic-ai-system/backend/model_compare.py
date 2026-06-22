from langchain_community.llms import Ollama
import time

models = ["llama3.1:8b"]

prompt = """
You are a customer support agent.

A customer says:

"My order has not arrived in 10 days. What should I do?"

Provide a professional customer support response.
"""

for model in models:
    print("\n" + "=" * 60)
    print(f"MODEL: {model}")

    llm = Ollama(model=model)

    start = time.time()

    response = llm.invoke(prompt)

    elapsed = time.time() - start

    print(f"\nTime Taken: {elapsed:.2f} seconds")
    print("\nResponse:\n")
    print(response[:500])