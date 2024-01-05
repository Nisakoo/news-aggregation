import logging
import logging_config

from telethon import TelegramClient, events
from utils.post import Post
from utils.tools import *

from config import *
from parsers.base_parser import BaseParser


logger = logging.getLogger(__name__)


class TelegramParser(BaseParser):
    def __init__(self, sources: list, callback: callable, **kwargs) -> None:
        self._sources = sources
        self._callback = callback

        self._client: TelegramClient = kwargs["client"]
        self._add_handlers()

        logger.info("Create TelegramParser")

    async def updates(self) -> None:
        raise NotImplementedError("Функция бесполезна, но без нее ничего не работает)")

    def _add_handlers(self) -> None:
        logger.info("Add handlers to TelegramParser")

        for source in self._sources:
            self._client.add_event_handler(
                self._new_posts_handler(source),
                events.NewMessage(chats=source)
            )

    def _new_posts_handler(self, post_source: str) -> callable:

        async def inner(event) -> None:
            logger.info("New message to TelegramParser")

            sender = await event.get_sender()

            await self._callback([
                Post(
                    title=sender.title,
                    content=event.raw_text,
                    source_name=sender.title,
                    source=post_source,
                    post_hash=get_hash(event.raw_text)
                )
            ])

        return inner