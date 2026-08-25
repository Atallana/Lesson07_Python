from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def checkout(self):
        # Нажмите Checkout.
        checkout = self.wait.until(EC.element_to_be_clickable((
                By.ID, "checkout"))
        )
        checkout.click()
