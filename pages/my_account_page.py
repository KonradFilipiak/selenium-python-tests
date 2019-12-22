from base.base_page import BasePage


class MyAccountPage(BasePage):

    def __init__(self):
        super(MyAccountPage, self).__init__("/index.php?controller=my-account")

    @property
    def order_history_and_details_button(self):
        return self.driver.find_element_by_xpath("//a[contains(@title, 'Orders')]")

    def is_initialized(self):
        return self.is_element_visible(self.order_history_and_details_button)