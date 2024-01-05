import html
import asyncio
import logging
import traceback
import logging_config

from telethon import TelegramClient

from config import *
from bot.telegram_bot import TelegramBot

from parsers.web_parser import WebParser
from parsers.telegram_parser import TelegramParser

from db.sqlite_db import SqliteDB


logger = logging.getLogger(__name__)


if __name__ == "__main__":
    db = SqliteDB(DB_FILE)

    try:
        with (
            TelegramClient("bot", API_ID, API_HASH) as bot,
            TelegramClient("anon", API_ID, API_HASH, system_version=SYSTEM_VERSION) as client
        ):
            telegram_bot = TelegramBot(bot, db, TELEGRAM_CHANNEL_NAME)
            web_parser = WebParser(WEB_SOURCES, telegram_bot.update_posts)
            telegram_parser = TelegramParser(TELEGRAM_SOURCES, telegram_bot.update_posts, client=client)

            loop = asyncio.get_event_loop()

            loop.run_until_complete(db.connect())
            tg_task = loop.create_task(telegram_bot.send_posts())
            wb_task = loop.create_task(web_parser.updates())

            loop.run_forever()
    except Exception as e:
        logger.error(f"Error has occurred {e}")

        loop = asyncio.get_event_loop()
        with TelegramClient("bot", API_ID, API_HASH) as bot:
            tb_list = traceback.format_exception(None, e, e.__traceback__)
            tb_string = "".join(tb_list)

            loop.run_until_complete(
                bot.send_message(ADMIN_ID, f"<pre>{html.escape(tb_string)}</pre>", parse_mode="HTML")
            )
    finally:
        asyncio.run(db.close())
        logger.info("END")