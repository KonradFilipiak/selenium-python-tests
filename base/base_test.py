import unittest

from managers import context
from managers.driver_manager import DriverManager
from utilities import utilities_methods


class BaseTest(unittest.TestCase):

    def setUp(self):
        utilities_methods.configure_logger()
        self.log = context.log
        self.log.info("{} -> Starting tests...".format(self.__class__))

        context.driver_manager = DriverManager()
        self.driver = context.driver_manager.driver
        self.wait = context.driver_manager.wait
        context.driver_manager.init_driver()

    def tearDown(self):
        context.driver_manager.quit()
        self.log.info("{} -> Ending tests...".format(self.__class__))
