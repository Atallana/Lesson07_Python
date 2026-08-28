import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.calc_page import CalculatorPage

@pytest.fixture
def driver():
    # Настройка браузера Google Chrome
    options = Options()
    # options.add_argument("--headless") # Раскомментируйте для запуска без графического окна
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(2)
    yield driver
    driver.quit()

def test_calc_page(driver):
    calc_page = CalculatorPage(driver, "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    calc_page.open_calc_page()
       
    # Устанавливаем задержку в 45 секунд через метод класса
    delay_time = "45"
    calc_page.set_delay(delay_time)
    
    # Проверяем, что значение задержки корректно ввелось
    assert calc_page.get_delay_value() == (delay_time)
    
    # Выполняем математическое действие: 7 + 8 =
    calc_page.click_button("7")
    calc_page.click_button("+")
    calc_page.click_button("8")
    calc_page.click_button("=")
    
    # Ожидаем результат с учетом выставленной задержки (45 секунд + запас)
    is_result_correct = calc_page.wait_for_result_text("15", timeout=46)
    
    assert is_result_correct, "Результат вычисления не равен 15 или не появился вовремя"
