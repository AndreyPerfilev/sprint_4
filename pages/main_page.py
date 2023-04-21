import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPageSamokat(BasePage):
    # Локаторы главной страницы
    button_header_order = [By.XPATH, "(//button[contains(.,'Заказать')])[1]"]
    button_body_order = [By.XPATH, "(//button[contains(.,'Заказать')])[2]"]

    button_question_one = [By.ID, "accordion__heading-0"]
    open_button_question_one = [By.ID, "accordion__panel-0"]

    button_question_two = [By.ID, "accordion__heading-1"]
    open_button_question_two = [By.ID, "accordion__panel-1"]

    button_question_three = [By.ID, "accordion__heading-2"]
    open_button_question_three = [By.ID, "accordion__panel-2"]

    button_question_four = [By.ID, "accordion__heading-3"]
    open_button_question_four = [By.ID, "accordion__panel-3"]

    button_question_five = [By.ID, "accordion__heading-4"]
    open_button_question_five = [By.ID, "accordion__panel-4"]

    button_question_six = [By.ID, "accordion__heading-5"]
    open_button_question_six = [By.ID, "accordion__panel-5"]

    button_question_seven = [By.ID, "accordion__heading-6"]
    open_button_question_seven = [By.ID, "accordion__panel-6"]

    button_question_eight = [By.ID, "accordion__heading-7"]
    open_button_question_eight = [By.ID, "accordion__panel-7"]
    logo_yandex = [By.CSS_SELECTOR, "[alt = 'Yandex']"]
    logo_samokat = [By.CSS_SELECTOR, "[alt = 'Scooter']"]
    title_main_page = [By.CSS_SELECTOR, "[class *= Home_Header]"]

    # МЕТОДЫ ГЛАВНОЙ СТРАНИЦЫ
    @allure.step('Кликаем на кнопку заказать в заголовке')
    def click_button_header_order(self):
        self.click_on_element(self.button_header_order)

    @allure.step('Кликаем на кнопку заказать со страницы')
    def click_button_body_order(self):
        self.click_on_element(self.button_body_order)

    @allure.step('Кликаем на 1-ый вопрос')
    def click_question_one(self):
        self.click_on_element(self.button_question_one)

    @allure.step('Кликаем на 2-ой вопрос')
    def click_question_two(self):
        self.click_on_element(self.button_question_two)

    @allure.step('Кликаем на 3-ий вопрос')
    def click_question_three(self):
        self.click_on_element(self.button_question_three)

    @allure.step('Кликаем на 4-ый вопрос')
    def click_question_four(self):
        self.click_on_element(self.button_question_four)

    @allure.step('Кликаем на 5-ый вопрос')
    def click_question_five(self):
        self.click_on_element(self.button_question_five)

    @allure.step('Кликаем на 6-ой вопрос')
    def click_question_six(self):
        self.click_on_element(self.button_question_six)

    @allure.step('Кликаем на 7-ой вопрос')
    def click_question_seven(self):
        self.click_on_element(self.button_question_seven)

    @allure.step('Кликаем на 8-ой вопрос')
    def click_question_eight(self):
        self.click_on_element(self.button_question_eight)

    # Методы возвращалки
    @allure.step('Получаем текст ответа на 1-ый вопрос')
    def get_text_question_one(self):
        return self.get_text_from_element(self.open_button_question_one)

    @allure.step('Получаем текст ответа на 2-ой вопрос')
    def get_text_question_two(self):
        return self.get_text_from_element(self.open_button_question_two)

    @allure.step('Получаем текст ответа на 3-ий вопрос')
    def get_text_question_three(self):
        return self.get_text_from_element(self.open_button_question_three)

    @allure.step('Получаем текст ответа на 4-ый вопрос')
    def get_text_question_four(self):
        return self.get_text_from_element(self.open_button_question_four)

    @allure.step('Получаем текст ответа на 5-ый вопрос')
    def get_text_question_five(self):
        return self.get_text_from_element(self.open_button_question_five)

    @allure.step('Получаем текст ответа на 6-ой вопрос')
    def get_text_question_six(self):
        return self.get_text_from_element(self.open_button_question_six)

    @allure.step('Получаем текст ответа на 7-ой вопрос')
    def get_text_question_seven(self):
        return self.get_text_from_element(self.open_button_question_seven)

    @allure.step('Получаем текст ответа на 8-ой вопрос')
    def get_text_question_eight(self):
        return self.get_text_from_element(self.open_button_question_eight)

    @allure.step('Скроллим к кнопке заказать со страницы')
    def scroll_to_body_order(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(By.CLASS_NAME, "Home_Status__YkfmH"))

    @allure.step('Кликаем на логотип Самокат')
    def open_samokat_page_by_logo(self):
        self.click_on_element(self.logo_samokat)

    @allure.step('Кликаем на логотип Яндекс')
    def open_ya_page_by_logo(self):
        self.click_on_element(self.logo_yandex)

    @allure.step('Получаем текст заголовка страницы')
    def get_text_title(self):
        return self.get_text_from_element(self.title_main_page)
