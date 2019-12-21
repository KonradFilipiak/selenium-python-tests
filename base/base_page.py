from abc import abstractmethod

import properties
from managers import context


class BasePage(object):

    def __init__(self, relative_url=""):
        self.driver = context.driver_manager.driver
        self.wait = context.driver_manager.wait
        self.relative_url = relative_url
        self.url = properties.base_url + relative_url

    @abstractmethod
    def is_initialized(self):
        pass

    def go_to(self):
        self.driver.get(self.url)
