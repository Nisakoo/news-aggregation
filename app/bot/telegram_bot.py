import asyncio
import logging
import logging_config

from telethon import TelegramClient

from config import *
from bot.base_bot import BaseBot
from bot.bot_messages import *

from db.base_db import BaseDB

from utils.post import Post


logger = logging.getLogger(__name__)


class TelegramBot(BaseBot):
    def __init__(self, bot: TelegramClient, db: BaseDB, channel_name: str) -> None:
        self._channel_name = channel_name
        self._db = db
        self._posts: list[Post] = list()

        self._client = bot
        logger.info("Create TelegramBot")
    
    async def update_posts(self, posts: list[Post]) -> None:
        logger.info("Update posts")
        for post in posts:
            if not (await self._db.is_posted(post.post_hash)):
                await self._db.insert_post(post)
                self._posts.append(post)

    async def send_posts(self) -> None:
        while True:
            if len(self._posts) > 0:
                logger.info("Send post")

                post = self._posts.pop()
                await self._client.send_message(
                    self._channel_name,
                    post_template(
                        post.title, post.content,
                        post.source_name, post.source
                    )
                )

            await asyncio.sleep(2)