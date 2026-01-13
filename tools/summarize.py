def summarize_text(text:str, max_chars: int = 500) -> str:
    """
    Simple deterministic summarizer.
    Trims text to a fixed size
    """

    if not text:
        return ""

    text = text.strip().replace("\n", " ")
    if len(text) <= max_chars:
        return text

    return text[:max_chars] + "..."
