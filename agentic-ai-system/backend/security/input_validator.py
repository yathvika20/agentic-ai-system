import re

# Maximum number of characters allowed in a user message
MAX_INPUT_LENGTH = 500

# Common prompt injection patterns
INJECTION_PATTERNS = [
    r"ignore\s+previous",
    r"system\s+prompt",
    r"reveal\s+instructions",
    r"developer\s+message",
    r"act\s+as",
    r"pretend\s+to\s+be",
    r"you\s+are\s+now",
    r"bypass",
    r"disable\s+safety",
]


def validate_input(user_input: str):
    """
    Validate user input before sending it to the LLM.

    Returns:
        (is_valid, reason)
    """

    # Check input length
    if len(user_input) > MAX_INPUT_LENGTH:
        return False, "Input too long."

    # Convert input to lowercase for matching
    text = user_input.lower()

    # Check for prompt injection patterns
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text):
            return False, "Potential prompt injection detected."

    return True, ""