from langfuse import Langfuse

langfuse = Langfuse(
    public_key="pk-lf-560008e1-3cf1-44de-b3be-ae10b435e5f6",
    secret_key="sk-lf-5140fffe-5a79-4372-9820-1fe2f2a26fbb",
    host="http://localhost:3000"
)

trace = langfuse.trace(
    name="test-trace"
)

trace.generation(
    name="llama",
    input="Hello",
    output="Hi there!"
)

langfuse.flush()

print("Trace sent successfully!")