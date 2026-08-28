from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    def fill_form(self):
        # Заполните форму своими данными:
        # имя,
        First_name_input = self.wait.until(EC.presence_of_element_located(
            (By.ID, "first-name"))
        )
        First_name_input.send_keys("Татьяна")

        # фамилия,
        Last_name_input = self.driver.find_element(By.ID, "last-name")
        Last_name_input.send_keys("Черкасова")

        # почтовый индекс.
        Postal_code_input = self.driver.find_element(By.ID, "postal-code")
        Postal_code_input.send_keys("185016")

    def go_to_total_page(self):
        # Нажмите кнопку Continue.
        continue_btn = self.wait.until(EC.element_to_be_clickable((
            By.ID, "continue"))
        )
        continue_btn.click()
