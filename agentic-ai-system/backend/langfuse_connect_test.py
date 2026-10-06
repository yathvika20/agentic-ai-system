import os
from dotenv import load_dotenv
from langfuse import Langfuse

load_dotenv()

lf = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

trace = lf.trace(name="test")

trace.generation(
    name="test-span",
    input="hello",
    output="hello"
)

lf.flush()

print("Langfuse connected OK")