from selenium.webdriver.support.wait import WebDriverWait

import properties
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class DriverManager:

    def __init__(self):
        browser = properties.browser

        if browser == "chrome":
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
        # TODO: add other browsers
        # TODO: and else: throw an exception or at least log that something is wrong (if I implement logger)

        self.wait = WebDriverWait(self.driver, properties.implicit_wait)

    def init_driver(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(properties.implicit_wait)