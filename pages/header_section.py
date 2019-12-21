from selenium.common.exceptions import NoSuchElementException

from base.base_page import BasePage


class HeaderSection(BasePage):

    def __init__(self):
        super(HeaderSection, self).__init__()

    @property
    def sign_in_button(self):
        return self.driver.find_element_by_xpath("//div[contains(@class, 'header_user_info')]/a[contains(@class, 'login')]")

    @property
    def sign_out_button(self):
        return self.driver.find_element_by_xpath("//div[contains(@class, 'header_user_info')]/a[contains(@class, 'logout')]")

    @property
    def contact_us_button(self):
        return self.driver.find_element_by_id("contact-link")

    def is_initialized(self):
        try:
            return self.contact_us_button.is_displayed()
        except NoSuchElementException:
            return False

    def is_user_logged_in(self):
        try:
            return self.sign_out_button.is_displayed()
        except NoSuchElementException:
            return False

    def is_user_logged_out(self):
        try:
            return self.sign_in_button.is_displayed()
        except NoSuchElementException:
            return False
