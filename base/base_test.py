import unittest

from managers import context
from managers.driver_manager import DriverManager


class BaseTest(unittest.TestCase):

    def setUp(self):
        context.driver_manager = DriverManager()
        self.driver = context.driver_manager.driver
        self.wait = context.driver_manager.wait
        context.driver_manager.init_driver()

    def tearDown(self):
        self.driver.quit()
