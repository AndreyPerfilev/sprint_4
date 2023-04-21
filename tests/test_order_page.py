import allure
import pytest
from selenium import webdriver
from pages.finish_page import FinishPage
from pages.main_page import MainPageSamokat
from pages.order_page import PageOrder
from pages.rent_page import PageRent


class TestOrderPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка оформления заказа')
    @pytest.mark.parametrize(
        'name,surname,address,metro,phone,day',
        [
            ['Гриб', 'подберезовик', 'лес за мкадом', 'ВДНХ', '79992223344', 'сутки'],
            ['Антон', 'Иванов', 'кунцевская ул', 'митино', '79992003040', 'двое суток']

        ]
    )
    def test_full_path_header_order(self, name, surname, address, metro, phone, day):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.click_button_header_order()
        test_order_page = PageOrder(self.driver)
        test_order_page.wait_load_page()
        test_order_page.send_name(name)
        test_order_page.send_sure_name(surname)
        test_order_page.send_address(address)
        test_order_page.send_metro_field(metro)
        test_order_page.send_phone(phone)
        test_order_page.click_button_next()
        test_page_rent = PageRent(self.driver)
        test_page_rent.wait_title()
        test_page_rent.select_day_rent_period(day)
        test_page_rent.click_black_samokat()
        test_page_rent.send_comment_for_courier("Звоните в домофон")
        test_page_rent.send_date_plus_three_days()
        test_page_rent.click_button_body_order()
        test_page_rent.click_yes_button()
        test_page_rent.click_look_status()
        test_finish_page = FinishPage(self.driver)
        button_cancel = test_finish_page.get_text_cancel_order()
        assert button_cancel == "Отменить заказ"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
