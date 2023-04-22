import time
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    def scroll_page_to_down(self):
        self.driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        self.wait_sec(0.5)

    @allure.step('Ожидаем {sec} секунд')
    def wait_sec(self, sec):
        time.sleep(sec)

    def send_data(self, locator, data):
        self.driver.find_element(*locator).send_keys(data)

    def wait_element(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получаем текущий URL')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Переключаем на {index} вкладку')
    def switch_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])
