from selenium.webdriver.support.wait import WebDriverWait

from managers import context
from utilities import properties
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:

    def __init__(self):
        self.log = context.log
        browser = properties.browser

        if browser == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.log.debug("Initializing {}".format(browser))
        # TODO: add other browsers
        # TODO: and else: throw an exception or at least log that something is wrong (if I implement logger)

        self.wait = WebDriverWait(self.driver, properties.implicit_wait)

    def init_driver(self):
        self.driver.maximize_window()
        self.log.debug("Maximizing browser window")

        self.driver.implicitly_wait(properties.implicit_wait)
        self.log.debug("Setting implicit wait to {} seconds".format(properties.implicit_wait))

    def quit(self):
        self.driver.quit()
        self.log.debug("Quiting the driver")
