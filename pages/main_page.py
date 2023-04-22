import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class MainPageLocators():
    # Локаторы главной страницы
    base_url = 'https://qa-scooter.praktikum-services.ru'
    button_header_order = [By.XPATH, "(//button[contains(.,'Заказать')])[1]"]
    button_body_order = [By.XPATH, "(//button[contains(.,'Заказать')])[2]"]
    logo_yandex = [By.CSS_SELECTOR, "[alt = 'Yandex']"]
    logo_samokat = [By.CSS_SELECTOR, "[alt = 'Scooter']"]
    title_main_page = [By.CSS_SELECTOR, "[class *= Home_Header]"]
    home_status = [By.CLASS_NAME, "Home_Status__YkfmH"]


class MainPageSamokat(BasePage):

    # МЕТОДЫ ГЛАВНОЙ СТРАНИЦЫ
    @allure.step('Открываем главную страницу')
    def open(self):
        self.driver.get(MainPageLocators.base_url)

    @allure.step('Кликаем на кнопку заказать в заголовке')
    def click_button_header_order(self):
        self.click_on_element(MainPageLocators.button_header_order)

    @allure.step('Кликаем на кнопку заказать со страницы')
    def click_button_body_order(self):
        self.click_on_element(MainPageLocators.button_body_order)

    @allure.step('Скроллим к кнопке заказать со страницы')
    def scroll_to_body_order(self):
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(*MainPageLocators.home_status))

    @allure.step('Кликаем на логотип Самокат')
    def open_samokat_page_by_logo(self):
        self.click_on_element(MainPageLocators.logo_samokat)

    @allure.step('Кликаем на логотип Яндекс')
    def open_ya_page_by_logo(self):
        self.click_on_element(MainPageLocators.logo_yandex)

    @allure.step('Получаем текст заголовка страницы')
    def get_text_title(self):
        return self.get_text_from_element(MainPageLocators.title_main_page)

    @allure.step("Кликаем по вопросу {index}")
    def click_question(self, index):
        question = [By.XPATH, "//div[@aria-controls='accordion__panel-" + str(index - 1) + "']"]
        self.click_on_element(question)

    @allure.step("Получаем ответ по вопросу  {index}")
    def return_answer(self, index):
        answer = [By.XPATH, "//div[@aria-labelledby='accordion__heading-" + str(index - 1) + "']"]
        return self.get_text_from_element(answer)
