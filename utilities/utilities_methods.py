import logging
import os
from datetime import datetime

from managers import context


def configure_logger():
    log_path = "logs/"
    file_name = "log-{}.log".format(datetime.now().time())
    log_format = "%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s"

    if not os.path.exists(log_path):
        os.makedirs(log_path)

    logging.basicConfig(filename=log_path + file_name,
                        format=log_format,
                        filemode="w",)

    context.log = logging.getLogger()

    context.log.setLevel(logging.INFO)