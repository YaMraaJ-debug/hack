import logging

logging.basicConfig(format='[%(asctime)s - %(levelname)s] - %(name)s : %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    level=logging.INFO)


class AsyncioFilter(logging.Filter):
    def filter(self, record):
        return (
            record.levelname != 'ERROR'
            or "Task was destroyed but it is pending!" not in record.msg
        )


asyncio_logger = logging.getLogger('asyncio')
asyncio_logger.addFilter(AsyncioFilter())

logging.getLogger('telethon').setLevel(logging.WARNING)
logging.captureWarnings(True)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
