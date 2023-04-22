import allure
import pytest

from pages.main_page import MainPageSamokat
from pages.order_page import PageOrder
from tests.data_tests.data import Data, Urls


class TestMainPage:

    @allure.title('Проверка кнопки заказать из заголовка')
    def test_button_header_order(self, driver):
        test_main_page = MainPageSamokat(driver)
        test_main_page.open()
        test_main_page.click_button_header_order()
        test_order_page = PageOrder(driver)
        test_order_page.wait_load_page()
        actual_title = test_order_page.get_title_text()
        assert actual_title == Data.main_page_title

    @allure.title('Проверка кнопки заказать со страницы')
    def test_button_body_order(self, driver):
        test_main_page = MainPageSamokat(driver)
        test_main_page.open()
        test_main_page.scroll_to_body_order()
        test_main_page.click_button_body_order()
        test_order_page = PageOrder(driver)
        test_order_page.wait_load_page()
        actual_title = test_order_page.get_title_text()
        assert actual_title == Data.main_page_title

    @allure.title('Проверка вопроса и текста ответа  для {index} вопроса')
    @pytest.mark.parametrize('index', [1, 2, 3, 4, 5, 6, 7, 8])
    def test_question_and_answer(self, index, driver):
        test_main_page = MainPageSamokat(driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question(index)
        answer = test_main_page.return_answer(index)
        data_answers = Data()
        answer_text = data_answers.return_answer(index)
        assert answer == answer_text

    @allure.title('Проверка перехода по логотипу Яндекс')
    def test_logo_yandex(self, driver):
        test_main_page = MainPageSamokat(driver)
        test_main_page.open()
        test_main_page.open_ya_page_by_logo()
        test_main_page.switch_tab(1)
        test_main_page.wait_sec(3)
        current_url = test_main_page.get_url()
        assert current_url == Urls.ya_main_page_url

    @allure.title('Проверка перехода по логотипу Самокат')
    def test_logo_samokat(self, driver):
        test_main_page = MainPageSamokat(driver)
        test_main_page.open()
        test_main_page.open_samokat_page_by_logo()
        title = test_main_page.get_text_title()
        assert title == Data.samokat_text_title
