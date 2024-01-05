class Post:
    def __init__(self, title: str="",
                 content: str="", source_name: str="",
                 source: str="", post_hash: int=0) -> None:
        self.title = title
        self.content = content
        self.source_name = source_name
        self.source = source
        self.post_hash = post_hash