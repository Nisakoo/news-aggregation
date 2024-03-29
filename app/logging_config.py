import logging.config


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base_formatter": {
            "format": "%(asctime)s %(levelname)s %(message)s",
        }
    },
    "handlers": {
        "stdout": {
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "formatter": "base_formatter",
        },
        "file": {
            "class": "logging.FileHandler",
            "filename": "news_agg.log",
            "formatter": "base_formatter",
            "encoding": "utf-8"
        }
    },
    "loggers": {
        "": {"handlers": ["file", "stdout"], "level": "DEBUG"}},
}

logging.config.dictConfig(LOGGING_CONFIG)