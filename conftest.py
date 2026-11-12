import pytest
from playwright.sync_api import sync_playwright, Browser, Page


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Global context args – applied to every test."""
    return {
        **browser_context_args,
        "base_url": "https://www.saucedemo.com",
        "viewport": {"width": 1280, "height": 720},
    }


@pytest.fixture
def login_page(page: Page):
    """Fixture that returns a ready LoginPage object."""
    from pages.login_page import LoginPage
    login_page = LoginPage(page)
    login_page.goto()
    return login_page