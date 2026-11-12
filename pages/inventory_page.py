from playwright.sync_api import Page


class InventoryPage:
    """Page Object for SauceDemo Inventory (Products) Page."""

    def __init__(self, page: Page):
        self.page = page
        self.page_title = page.locator(".title")
        self.backpack_add_button = page.locator(
            '[data-test="add-to-cart-sauce-labs-backpack"]'
        )
        self.cart_icon = page.locator(".shopping_cart_link")
        self.cart_badge = page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.backpack_add_button.click()

    def go_to_cart(self):
        self.cart_icon.click()

    def get_cart_count(self) -> str:
        return self.cart_badge.text_content() or "0"