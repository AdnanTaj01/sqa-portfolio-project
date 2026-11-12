from playwright.sync_api import Page


class CartPage:
    """Page Object for SauceDemo Cart Page."""

    def __init__(self, page: Page):
        self.page = page
        self.checkout_button = page.locator('[data-test="checkout"]')
        self.cart_items = page.locator(".cart_item")

    def proceed_to_checkout(self):
        self.checkout_button.click()

    def get_cart_item_count(self) -> int:
        return self.cart_items.count()