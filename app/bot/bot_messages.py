from bot.raw_messages import *


def post_template(title: str, content: str, source_name: str, source_link: str) -> str:
    
    
    return POST_TEMPLATE.format(
        title=title,
        content=content,
        source_name=source_name,
        source_link=source_link
    )