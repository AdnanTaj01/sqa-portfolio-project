from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


def test_end_to_end_purchase_flow(page: Page):
    """E2E: Login → Add to cart → Checkout."""

    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)

    # Step 1: Login
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # Step 2: Add item to cart
    inventory_page.add_backpack_to_cart()
    expect(inventory_page.cart_badge).to_have_text("1")

    # Step 3: Go to cart
    inventory_page.go_to_cart()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    assert cart_page.get_cart_item_count() == 1

    # Step 4: Checkout
    cart_page.proceed_to_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")