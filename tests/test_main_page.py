from selenium import webdriver
from pages.main_page import MainPageSamokat
from pages.order_page import PageOrder
import allure


class TestMainPage:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @allure.title('Проверка кнопки заказать из заголовка')
    def test_button_header_order(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.click_button_header_order()
        test_order_page = PageOrder(self.driver)
        test_order_page.wait_load_page()
        actual_title = test_order_page.get_title_text()
        assert actual_title == "Для кого самокат"

    @allure.title('Проверка кнопки заказать со страницы')
    def test_button_body_order(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_to_body_order()
        test_main_page.click_button_body_order()
        test_order_page = PageOrder(self.driver)
        test_order_page.wait_load_page()
        actual_title = test_order_page.get_title_text()
        assert actual_title == "Для кого самокат"

    @allure.title('Проверка текста для 1-го вопроса')
    def test_first_question(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question_one()
        question_one = test_main_page.get_text_question_one()
        assert question_one == "Сутки — 400 рублей. Оплата курьеру — наличными или картой."

    @allure.title('Проверка текста для 2-го вопроса')
    def test_two_question(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question_two()
        question_two = test_main_page.get_text_question_two()
        assert question_two == "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, " \
                               "можете просто сделать несколько заказов — один за другим."

    @allure.title('Проверка текста для 3-го вопроса')
    def test_three_question(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question_three()
        question_three = test_main_page.get_text_question_three()
        assert question_three == "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. " \
                                 "Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. " \
                                 "Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."

    @allure.title('Проверка текста для 4-го вопроса')
    def test_four_question(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question_four()
        question_four = test_main_page.get_text_question_four()
        assert question_four == "Только начиная с завтрашнего дня. Но скоро станем расторопнее."

    @allure.title('Проверка текста для 5-го вопроса')
    def test_five_question(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question_five()
        question_five = test_main_page.get_text_question_five()
        assert question_five == "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку" \
                                " по красивому номеру 1010."

    @allure.title('Проверка текста для 6-го вопроса')
    def test_six_question(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question_six()
        question_six = test_main_page.get_text_question_six()
        assert question_six == "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток —" \
                               " даже если будете кататься без передышек и во сне. Зарядка не понадобится."

    @allure.title('Проверка текста для 7-го вопроса')
    def test_seven_question(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question_seven()
        question_seven = test_main_page.get_text_question_seven()
        assert question_seven == "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не" \
                                 " попросим. Все же свои."

    @allure.title('Проверка текста для 8-го вопроса')
    def test_eight_question(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.scroll_page_to_down()
        test_main_page.click_question_eight()
        question_eight = test_main_page.get_text_question_eight()
        assert question_eight == "Да, обязательно. Всем самокатов! И Москве, и Московской области."

    @allure.title('Проверка перехода по логотипу Яндекс')
    def test_logo_yandex(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.open_ya_page_by_logo()
        test_main_page.switch_tab(1)
        test_main_page.wait_sec(3)
        current_url = test_main_page.get_url()
        assert current_url == "https://dzen.ru/?yredirect=true"

    @allure.title('Проверка перехода по логотипу Самокат')
    def test_logo_samokat(self):
        test_main_page = MainPageSamokat(self.driver)
        test_main_page.open()
        test_main_page.open_samokat_page_by_logo()
        title = test_main_page.get_text_title()
        assert title == "Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
