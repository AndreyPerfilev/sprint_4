import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class PageOrder(BasePage):
    # Локаторы страницы заказа
    name_field = [By.CSS_SELECTOR, "input[placeholder*='Имя']"]
    sure_name_field = [By.CSS_SELECTOR, "input[placeholder*='Фамилия']"]
    address_field = [By.CSS_SELECTOR, "input[placeholder *= 'Адрес']"]
    metro_field = [By.CSS_SELECTOR, "input[placeholder *= 'Станция метро']"]
    telephone_field = [By.CSS_SELECTOR, "input[placeholder *= 'Телефон']"]
    button_next = [By.XPATH, "//button[contains(text(),'Далее')]"]
    title_order_page = [By.CSS_SELECTOR, "[class*='Order_Header']"]
    drop_list_metro_station = [By.CLASS_NAME, 'select-search__select']
    first_element_on_list = [By.XPATH, '//ul[@class="select-search__options"]/li/button']

    # методы страницы заказа
    @allure.step('Заполняем поле имя значением {data}')
    def send_name(self, data):
        self.send_data(self.name_field, data)

    @allure.step('Заполняем поле фамилия значением {data}')
    def send_sure_name(self, data):
        self.send_data(self.sure_name_field, data)

    @allure.step('Заполняем поле адрес значением {data}')
    def send_address(self, data):
        self.send_data(self.address_field, data)

    @allure.step('Заполняем поле метро значением {data}')
    def send_metro_field(self, data):
        self.send_data(self.metro_field, data)
        self.click_on_element(self.first_element_on_list)

    @allure.step('Заполняем поле телефон значением {data}')
    def send_phone(self, data):
        self.send_data(self.telephone_field, data)

    @allure.step('Кликаем на кнопку далее')
    def click_button_next(self):
        self.click_on_element(self.button_next)

    @allure.step('Ожидаем загрузку страницы оформления заказа')
    def wait_load_page(self):
        self.wait_element(self.title_order_page)

    @allure.step('Получаем тест заголовка страницы оформления заказа')
    def get_title_text(self):
        return self.get_text_from_element(self.title_order_page)
