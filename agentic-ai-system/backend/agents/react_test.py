from backend.agents.react_agent import run_agent


query = "What is the return policy?"

result = run_agent(query)

print("\nQuestion:")
print(query)

print("\nAnswer:")
print(result["answer"])

print("\nMessages exchanged:")
print(len(result["steps"]))