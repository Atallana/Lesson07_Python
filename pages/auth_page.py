from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 5)

    def open(self):
        self.driver.get(self.url)

    def login(self, user_name, password):
        username_input = self.wait.until(EC.presence_of_element_located(
                (By.ID, "user-name"))
        )
        username_input.send_keys(user_name)

        password_input = self.driver.find_element(By.ID, "password")
        password_input.send_keys(password)

        login = self.wait.until(EC.element_to_be_clickable((
                By.ID, "login-button"))
        )
        login.click()
