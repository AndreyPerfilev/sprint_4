import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class FinishPage(BasePage):
    track_page = [By.XPATH, '//button[contains(.,"Отменить заказ")]']

    @allure.step('Получаем текст кнопки отмены заказа')
    def get_text_cancel_order(self):
        return self.get_text_from_element(self.track_page)
