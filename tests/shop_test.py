from selenium import webdriver
from pages.auth_page import AuthPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.form_page import FormPage
from pages.total_page import TotalPage



def test_shop_page():
    driver = webdriver.Firefox()
    auth_page = AuthPage(driver, "https://www.saucedemo.com/")
    auth_page.open()
    auth_page.login('standard_user', 'secret_sauce')

    inventory_page = InventoryPage(driver)
    inventory_page.add_to_cart()
    inventory_page.click_cart()

    cart_page = CartPage(driver)
    cart_page.checkout

    form_page = FormPage(driver)
    form_page.fill_form
    form_page.go_to_total_page

    total_page = TotalPage(driver)
    total_page.check_total

    assert total_page.check_total

    driver.quit()