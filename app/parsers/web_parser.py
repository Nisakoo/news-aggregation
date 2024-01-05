import asyncio
import logging
import logging_config
from collections import deque

import httpx
from lxml import etree
from bs4 import BeautifulSoup

from parsers.base_parser import BaseParser
from utils.post import Post
from utils.tools import *
from utils.web_source import WebSource


logger = logging.getLogger(__name__)


class WebParser(BaseParser):
    def __init__(self, sources: list[WebSource], callback: callable) -> None:
        self._sources = sources
        self._callback = callback
        self._posted = deque(maxlen=50)

        logger.info("Create WebParser")

    async def updates(self) -> None:
        while True:
            posts = list()
            for source in self._sources:
                for post in await source.parse_func(source.source, self._posted):
                    post.source_name = source.name
                    post.source = source.source
                    post.post_hash = get_hash(post.title)

                    posts.append(post)
                    self._posted.appendleft(post.post_hash)

            if len(posts) > 0:
                logger.info("Send posts to TelegramBot from WebParser")
                await self._callback(posts)

            await asyncio.sleep(10)
    
    @staticmethod
    async def tiu_parser(source: str, posted: deque) -> list[Post]:
        logger.info("Run TIU parser")
        
        r = httpx.get(source)
        soup = BeautifulSoup(r.content, "html.parser")

        posts = list()
        for post in soup.find_all("div", class_="media-body"):
            link = post.find("a")

            news_url = link["href"]
            title = link.text
            
            if not (get_hash(title) in posted):
                r = httpx.get(news_url)
                soup = BeautifulSoup(r.content, "html.parser")

                news_content = str()
                for text_block in soup.find_all("p", style=True, text=True):
                    news_content += text_block.text

                news_content = ". ".join(news_content.split(".")[:2]) + "..."

                posts.append(Post(
                    title=title,
                    content=news_content,
                ))

        return posts