from abc import ABC, abstractmethod

from utils.post import Post


class BaseDB(ABC):
    @abstractmethod
    def __init__(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def connect(self) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def insert_post(self, post: Post) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def is_posted(self, post_hash: int) -> bool:
        raise NotImplementedError()
    
    @abstractmethod
    async def close(self) -> None:
        raise NotImplementedError()