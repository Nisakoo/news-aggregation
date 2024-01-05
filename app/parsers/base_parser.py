from typing import Any

from abc import ABC, abstractmethod


class BaseParser(ABC):
    @abstractmethod
    def __init__(self, sources: Any, callback: callable, **kwargs) -> None:
        raise NotImplementedError()
    
    @abstractmethod
    async def updates(self) -> None:
        raise NotImplementedError()