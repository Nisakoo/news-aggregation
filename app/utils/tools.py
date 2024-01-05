def get_hash(content: str) -> str:
    return content.replace(" ", "")[:64]