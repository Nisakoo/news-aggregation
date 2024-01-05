class WebSource:
    def __init__(self, name: str, source: str, parse_func: callable) -> None:
        self.name = name
        self.source = source
        self.parse_func = parse_func