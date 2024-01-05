from abc import ABC, abstractmethod

from utils.post import Post


class BaseBot(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def update_posts(self, posts: list[Post]) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def send_posts(self) -> None:
        raise NotImplementedError()