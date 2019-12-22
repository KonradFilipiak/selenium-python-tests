from abc import abstractmethod

from selenium.common.exceptions import NoSuchElementException

from utilities import properties
from managers import context


class BasePage(object):

    def __init__(self, relative_url=""):
        self.log = context.log

        self.driver = context.driver_manager.driver
        self.wait = context.driver_manager.wait

        self.relative_url = relative_url
        self.url = properties.base_url + relative_url
        self.log.debug("Setting url of {} to: {}".format(self.__class__, self.url))

    @abstractmethod
    def is_initialized(self):
        pass

    def go_to(self):
        self.driver.get(self.url)
        self.log.info("Going to: {} ({})".format(self.url, self.__class__))

    def is_element_visible(self, element):
        try:
            return element.is_displayed()
        except NoSuchElementException:
            return False
