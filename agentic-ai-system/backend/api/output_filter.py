import re

# Replace with actual competitor names if needed
COMPETITOR_NAMES = [
    "CompetitorA",
    "CompetitorB"
]


def filter_output(text: str, context: dict = None) -> str:
    """
    Filters sensitive information from LLM responses.
    """

    # Remove competitor names
    for name in COMPETITOR_NAMES:
        if name.lower() in text.lower():
            text = re.sub(
                name,
                "[Competitor]",
                text,
                flags=re.IGNORECASE
            )

    # Remove email addresses
    email_pattern = (
        r"\b[A-Za-z0-9._%+-]+"
        r"@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    )

    emails = re.findall(email_pattern, text)

    for email in emails:
        text = text.replace(
            email,
            "[Email Redacted]"
        )

    return text