from base.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class SignInPage(BasePage):

    def __init__(self):
        super(SignInPage, self).__init__("/index.php?controller=authentication&back=my-account")

    @property
    def email_input(self):
        return self.driver.find_element_by_id("email")

    @property
    def password_input(self):
        return self.driver.find_element_by_id("passwd")

    @property
    def sign_in_button(self):
        return self.driver.find_element_by_id("SubmitLogin")

    @property
    def login_error_message(self):
        return self.driver.find_element_by_xpath("//div[contains(@class, 'alert alert-danger')]/ol")

    def is_initialized(self):
        try:
            return self.sign_in_button.is_displayed()
        except NoSuchElementException:
            return False

    def log_in(self, email, password):
        self.email_input.send_keys(email)
        self.password_input.send_keys(password)
        self.sign_in_button.click()
