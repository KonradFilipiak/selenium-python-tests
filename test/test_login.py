from parameterized import parameterized

import properties
from base.base_test import BaseTest
from pages.header_section import HeaderSection
from pages.my_account_page import MyAccountPage
from pages.sign_in_page import SignInPage


class LoginTests(BaseTest):

    def setUp(self):
        super(LoginTests, self).setUp()
        self.sign_in_page = SignInPage()
        self.my_account_page = MyAccountPage()
        self.header_section = HeaderSection()

        self.sign_in_page.go_to()

    def test_user_can_log_in_with_good_credentials(self):
        self.sign_in_page.log_in(properties.user_email, properties.user_password)

        self.assertTrue(self.header_section.is_user_logged_in())
        self.assertTrue(self.my_account_page.is_initialized())

    @parameterized.expand([
        [properties.user_email, "WrongPassword1!", "Authentication failed."],
        [properties.user_email, "", "Password is required."],
        ["", properties.user_password, "An email address required."],
        ["invalid-email", properties.user_password, "Invalid email address."],
        ["example-of-wrong-email@konradfilipiak.com", properties.user_password, "Authentication failed."],
        ["", "", "An email address required."]
    ])
    def test_user_cannot_log_in_with_wrong_credentials(self, email, password, error_message):
        self.sign_in_page.log_in(email, password)

        self.assertEqual(self.sign_in_page.login_error_message.text, error_message)
        self.assertTrue(self.header_section.is_user_logged_out())

