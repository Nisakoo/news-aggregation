import logging
import logging_config

import aiosqlite
from utils.post import Post

from db.base_db import BaseDB
from db.sql_commands import *


logger = logging.getLogger(__name__)


class SqliteDB(BaseDB):
    def __init__(self, db_file: str) -> None:
        self._db_file = db_file

    async def connect(self) -> None:
        logger.info("Connect to SqliteDB")

        self._db = await aiosqlite.connect(self._db_file)
        await self._create_table()


    async def insert_post(self, post: Post) -> None:
        logger.info("Insert post to DB")

        values = (post.title, post.content, post.source, post.post_hash)
        await self._db.execute(INSERT_VALUES_SQL, values)
        await self._db.commit()

    async def is_posted(self, post_hash: int) -> bool:
        logger.info("Check if post is posted")

        rows = await self._db.execute_fetchall(IS_POSTED_SQL, (post_hash,))
        return len(rows) > 0

    async def close(self) -> None:
        logger.info("Close connection to SqliteDB")

        await self._db.close()

    async def _create_table(self) -> None:
        await self._db.execute(CREATE_TABLE_SQL)