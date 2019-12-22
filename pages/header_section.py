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
        return self.is_element_visible(self.contact_us_button)

    def is_user_logged_in(self):
        return self.is_element_visible(self.sign_out_button)

    def is_user_logged_out(self):
        return self.is_element_visible(self.sign_in_button)
