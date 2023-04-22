from datetime import datetime

import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class RentPageLocators:
    when_income_samokat = [By.CSS_SELECTOR, "input[placeholder *= 'Когда']"]
    rental_period = [By.CLASS_NAME, "Dropdown-placeholder"]
    colour_samokat_black = [By.ID, "black"]
    comment_for_courier = [By.CSS_SELECTOR, "input[placeholder *= 'Комментарий']"]
    button_body_order = [By.XPATH, "(//button[contains(.,'Заказать')])[2]"]
    button_yes = [By.XPATH, "//button[contains(.,'Да')]"]
    look_status = [By.XPATH, "//button[contains(.,'статус')]"]
    make_scr = [By.XPATH, "//button[contains(.,'статус')]"]
    title_rent = [By.CSS_SELECTOR, "[class*='Order_Header']"]


class RentPage(BasePage):
    # Локаторы страницы аренды

    # Методы страницы аренды
    def calculate_plus_three_days_for_order(self):
        current_date = datetime.now().date()
        month = str(0) + str(current_date.month) if len(str(current_date.month)) < 2 else str(current_date.month)
        date_plus_two_days = str(current_date.day + 3) + "." + month + "." + str(current_date.year)
        normal_current_date = date_plus_two_days.replace("-", ".")
        return normal_current_date

    @allure.step('Отправляет дату + 3 дня от сегодня')
    def send_date_plus_three_days(self):
        self.send_data(RentPageLocators.when_income_samokat, self.calculate_plus_three_days_for_order())

    @allure.step('Выбор черного самоката')
    def click_black_samokat(self):
        self.click_on_element(RentPageLocators.colour_samokat_black)

    @allure.step('Заполняем комментарий для курьера {data}')
    def send_comment_for_courier(self, data):
        self.send_data(RentPageLocators.comment_for_courier, data)

    @allure.step('Нажимаем кнопку оформить заказ')
    def click_button_body_order(self):
        self.click_on_element(RentPageLocators.button_body_order)

    @allure.step('Нажимаем кнопку да')
    def click_yes_button(self):
        self.click_on_element(RentPageLocators.button_yes)

    @allure.step('Нажимаем кнопку посмотреть статус заказа')
    def click_look_status(self):
        self.click_on_element(RentPageLocators.look_status)

    @allure.step('Ожидаем страницу про аренду')
    def wait_title(self):
        self.wait_element(RentPageLocators.title_rent)

    @allure.step('Выбираем период аренды: {text}')
    def select_day_rent_period(self, text):
        self.click_on_element(RentPageLocators.rental_period)
        day = [By.XPATH, "//div[contains(text(), '" + text + "')]"]
        self.click_on_element(day)
