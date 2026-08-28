from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def add_to_cart(self):    
        # Добавьте в корзину товары:
        # Sauce Labs Backpack.
        sauce_Labs_Backpack = self.wait.until(EC.element_to_be_clickable((
            By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        sauce_Labs_Backpack.click()

        # Sauce Labs Bolt T-Shirt.
        sauce_Labs_Bolt_T_Shirt = self.wait.until(EC.element_to_be_clickable((
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))
        )
        sauce_Labs_Bolt_T_Shirt.click()

        # Sauce Labs Onesie.
        sauce_Labs_Onesie = self.wait.until(EC.element_to_be_clickable((
            By.ID, "add-to-cart-sauce-labs-onesie"))
        )
        sauce_Labs_Onesie.click()

    def click_cart(self):
        # Перейдите в корзину.
        shopping_cart_link = self.wait.until(EC.element_to_be_clickable((
            By.CLASS_NAME, "shopping_cart_link"))
        )
        shopping_cart_link.click()
