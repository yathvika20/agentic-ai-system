import re
from fastapi import HTTPException

INJECTION_PATTERNS = [
    r"ignore (all )?(previous|prior|above) instructions",
    r"you are now",
    r"disregard your",
    r"act as (a|an) ?different",
    r"reveal (your|the )?system prompt",
]


def validate_input(text: str) -> str:
    """
    Validate incoming user input.
    Raises HTTPException if invalid.
    """

    if len(text) > 2000:
        raise HTTPException(
            status_code=400,
            detail="Message too long (max 2000 characters)."
        )

    text_lower = text.lower()

    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            raise HTTPException(
                status_code=400,
                detail="Message contains invalid content."
            )

    return text.strip()


def validate_output(text: str) -> str:
    """
    Truncate extremely long model outputs.
    """

    if len(text) > 5000:
        return text[:5000] + " ... [truncated]"

    return text