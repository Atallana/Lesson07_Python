from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 15)
    
        # Локаторы элементов
        self.DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    
        # Динамический локатор для кнопок калькулятора (цифры и знаки)
        self.BUTTON_XPATH = "//span[text()='{text}']"

        self.SCREEN = (By.CSS_SELECTOR, ".screen")


    def open_calc_page(self):
        # Открыть страницу калькулятора
        self.driver.get(self.url)
        return self

    def set_delay(self, seconds):
        # Установить значение в поле ввода задержки (#delay)
        delay_field = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        delay_field.clear()
        delay_field.send_keys(seconds)
        return self

    def get_delay_value(self):
        # Получить текущее значение из поля задержки
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.DELAY_INPUT)
        )
        return delay_field.get_attribute("value")

    def click_button(self, button_text: str):
    # Кликнуть по кнопке калькулятора
        xpath = self.BUTTON_XPATH.format(text=button_text)
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        button.click()
        return self

    def wait_for_result_text(self, expected_text, timeout):
        # Дождаться появления конкретного результата на экране
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        )