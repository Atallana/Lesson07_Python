from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TotalPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)  

    def check_total(self):
        # Прочитайте со страницы итоговую стоимость (Total).
        self.wait.until(EC.visibility_of_element_located((
        By.CSS_SELECTOR, ".summary_total_label"))
        )

        # Проверьте, что итоговая сумма равна $58.29.
        return self.wait.until(
            EC.text_to_be_present_in_element((
                By.CSS_SELECTOR, ".summary_total_label"), "$58.29")
        )
