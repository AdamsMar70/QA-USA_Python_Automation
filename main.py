import data
import helpers
from selenium import webdriver
from pages import UrbanRoutesPage
import time


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        # do not modify - we need additional logging enabled in order to retrieve phone confirmation code
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL):
            print("Connected to the Urban Routes server")
        else:
            print("Cannot connect to Urban Routes. Check the server is on and still running")

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        assert routes_page.get_from_address() == data.ADDRESS_FROM
        assert routes_page.get_to_address() == data.ADDRESS_TO

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.input_call_taxi()
        routes_page.input_supportive_tcard_title()
        assert "Supportive" in routes_page.get_supportive_tcard_title()

    def test_fill_phone_number(self, routes_page=None):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.input_call_taxi()
        routes_page.input_supportive_tcard_title()
        routes_page.click_phone_number_button()
        routes_page.input_phone_number(data.PHONE_NUMBER)
        routes_page.click_phone_number_next_button()
        time.sleep(1)
        routes_page.input_phone_code()
        routes_page.click_phone_code_confirm_button()
        assert routes_page.get_phone_number() == data.PHONE_NUMBER


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page: UrbanRoutesPage = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.input_call_taxi()
        routes_page.input_supportive_tcard_title()
        routes_page.click_card_number_button()
        routes_page.add_card_number()
        routes_page.input_card_number(data.CARD_NUMBER)
        routes_page.input_card_code(data.CARD_CODE)
        routes_page.card_number_link_button()
        routes_page.click_card_number_close_button()
        assert routes_page.get_card_number() == data.CARD_NUMBER

    def test_message_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.input_call_taxi()
        routes_page.input_supportive_tcard_title()
        routes_page.input_message_for_driver(data.MESSAGE_FOR_DRIVER)
        assert routes_page.get_message_for_driver()== data.MESSAGE_FOR_DRIVER

    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.input_call_taxi()
        routes_page.input_supportive_tcard_title()
        routes_page.order_blanket_and_handkerchiefs()
        routes_page.get_order_blanket_and_handkerchiefs()
        assert routes_page.get_order_blanket_and_handkerchiefs()

    def test_order_ice_cream(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.input_call_taxi()
        routes_page.input_supportive_tcard_title()
        time.sleep(2)
        routes_page.order_ice_cream_counter()
        expect = '2'
        assert routes_page.get_order_ice_cream() == expect


    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.input_from_address(data.ADDRESS_FROM)
        routes_page.input_to_address(data.ADDRESS_TO)
        routes_page.input_call_taxi()
        routes_page.input_supportive_tcard_title()
        routes_page.click_phone_number_button()
        routes_page.input_phone_number(data.PHONE_NUMBER)
        routes_page.click_phone_number_next_button()
        time.sleep(1)
        routes_page.input_phone_code()
        routes_page.click_phone_code_confirm_button()
        routes_page.click_card_number_button()
        routes_page.add_card_number()
        routes_page.input_card_number(data.CARD_NUMBER)
        routes_page.input_card_code(data.CARD_CODE)
        routes_page.card_number_link_button()
        routes_page.click_card_number_close_button()
        routes_page.input_message_for_driver(data.MESSAGE_FOR_DRIVER)
        routes_page.order_blanket_and_handkerchiefs()
        routes_page.get_order_blanket_and_handkerchiefs()
        time.sleep(2)
        routes_page.order_ice_cream_counter()
        expect = '2'
        routes_page.click_ordering_a_taxi_button()
        routes_page.ordering_a_taxi_car_search_modal()
        assert routes_page.get_ordering_a_taxi_car_search_modal()



    @classmethod
    def teardown_class(cls):
        cls.driver.quit()