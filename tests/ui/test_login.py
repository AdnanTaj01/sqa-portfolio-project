import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


class TestLogin:
    """Login functionality test suite."""

    def test_valid_login_success(self, page: Page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")

        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(page.locator(".title")).to_have_text("Products")

    def test_invalid_credentials_error(self, page: Page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("invalid_user", "wrong_password")

        expect(login_page.error_message).to_be_visible()
        expect(login_page.error_message).to_contain_text(
            "Username and password do not match"
        )

    def test_empty_credentials_error(self, page: Page):
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("", "")

        expect(login_page.error_message).to_contain_text("Username is required")

    @pytest.mark.parametrize(
        "username,password,should_pass",
        [
            ("standard_user", "secret_sauce", True),
            ("locked_out_user", "secret_sauce", False),
            ("problem_user", "secret_sauce", True),
            ("wrong_user", "wrong_pass", False),
        ],
    )
    def test_login_data_driven(
        self, page: Page, username: str, password: str, should_pass: bool
    ):
        """Data-driven login test covering multiple scenarios."""
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(username, password)

        if should_pass:
            expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        else:
            expect(login_page.error_message).to_be_visible()