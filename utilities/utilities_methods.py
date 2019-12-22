import logging

from managers import context


def configure_logger():
    file_name = "logs.log"
    log_format = "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"

    logging.basicConfig(filename=file_name,
                        format=log_format,
                        filemode="a", )

    context.log = logging.getLogger()

    context.log.setLevel(logging.INFO)

