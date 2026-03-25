import time
from typing import Literal

import click
import driver
import phone
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import helpers
from helpers import retrieve_phone_code

class UrbanRoutesPage:

    # Locators Test 1
    FROM_FIELD = (By.ID, 'from')
    TO_FIELD = (By.ID, 'to')

    # Locators Test 2
    CALL_TAXI = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_TCARD_TITLE = (By.XPATH, '//div[@class="tcard"]//div[text()="Supportive"]')
    SUPPORTIVE_ACTIVE_TITLE = (By.XPATH, '//div[@class="tcard active"]')

    # Locator Test 3
    PHONE_NUMBER_BUTTON = (By.XPATH, '//div[@class="np-text"]')
    PHONE_NUMBER = (By.ID, 'phone')
    PHONE_NUMBER_NEXT_BUTTON = (By.CSS_SELECTOR, '.full')
    PHONE_CODE = (By.XPATH, '//input[@id="code"]')
    PHONE_CODE_CLICK_CONFIRM_BUTTON = (By.XPATH, '//button[contains(text(),"Confirm")]')

    # Locator Test 4
    CARD_NUMBER_BUTTON = (By.XPATH, '//div[@class="pp-text"]')
    ADD_CARD_NUMBER = (By.XPATH, '//div[@class="pp-plus-container"]')
    CARD_NUMBER = (By.ID, 'number')
    CARD_CODE = (By.XPATH, '//input[@class="card-input" and @id="code"]')
    CARD_NUMBER_LINK_BUTTON = (By.XPATH, '//button[contains(text(),"Link")]')
    CARD_NUMBER_CLOSE_BUTTON = (By.XPATH, '//div[@class="payment-picker open"]//button[@class="close-button section-close"]')

    # Locator Test 5
    MESSAGE_FOR_DRIVER = (By.XPATH, '//input[@id="comment"]')

    #Locators Test 6
    ORDER_BLANKET_AND_HANDKERCHIEFS = (By.CLASS_NAME, 'switch')
    ORDER_BLANKET_CHECKBOX = (By.XPATH, "//div[contains(@class,'r-sw-container')][.//div[normalize-space()='Blanket and handkerchiefs']]//input[@type='checkbox']")

    # Locator Test 7
    #ORDER_ICE_CREAM_PLUS_BUTTON = (By.XPATH, '//div[@class="counter_plus"]//div[@class="counter-value"]')
    #ORDER_ICE_CREAM_COUNTER = (By.XPATH, '//div[@class="reqs-head"]//div[@class="reqs-arrow open"]//div[@class="tariff-picker shown"]//button[@class="arrow-button tariffs-arrow-button"]//div[@class'"r-counter")

    ORDER_ICE_CREAM_PLUS_BUTTON = (By.XPATH, '//div[contains(@class, "counter")]//div[contains(@class, "plus")]')
    ORDER_ICE_CREAM_COUNTER = (By.XPATH, '//div[@class="counter-value"]')

     # Locator Test 8
    ORDERING_A_TAXI_BUTTON = (By.XPATH, '//div[@class="smart-button-wrapper"]//button[@class="smart-button"]')
    ORDERING_A_TAXI_CAR_SEARCH_MODAL = (By.XPATH, '//div[@class="order-body"]//div[@class="order-buttons"]//button[@class="order-button"]')



    def __init__(self, driver):
        self.driver = driver

    def input_from_address(self, from_address):
        self.driver.find_element(*self.FROM_FIELD).send_keys(from_address)

    def input_to_address(self, to_address):
        self.driver.find_element(*self.TO_FIELD).send_keys(to_address)

    def get_from_address(self):
        return self.driver.find_element(*self.FROM_FIELD).get_property('value')

    def get_to_address(self):
        return self.driver.find_element(*self.TO_FIELD).get_property('value')

    def input_call_taxi(self):
        time.sleep(2)
        self.driver.find_element(*self.CALL_TAXI).click()

    def input_supportive_tcard_title(self):
        self.driver.find_element(*self.SUPPORTIVE_TCARD_TITLE).click()
        time.sleep(2)

    def get_supportive_tcard_title(self):
        return self.driver.find_element(*self.SUPPORTIVE_ACTIVE_TITLE).text

    def input_supportive_active_title(self):
        self.driver.find_element(*self.SUPPORTIVE_TCARD_TITLE).click()

    def get_supportive_active_title(self):
        return self.driver.find_element(*self.SUPPORTIVE_ACTIVE_TITLE).text

    def click_phone_number_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_BUTTON).click()

    def input_phone_number(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER).send_keys(phone_number)

    def get_phone_number(self):
        return self.driver.find_element(*self.PHONE_NUMBER_BUTTON).text

    def click_phone_number_next_button(self):
        self.driver.find_element(*self.PHONE_NUMBER_NEXT_BUTTON).click()

    def input_phone_code(self):
        phone_code = helpers.retrieve_phone_code(self.driver)
        self.driver.find_element(*self.PHONE_CODE).send_keys(phone_code)

    def click_phone_code_confirm_button(self):
        self.driver.find_element(*self.PHONE_CODE_CLICK_CONFIRM_BUTTON).click()

    def card_number_button(self):
        self.driver.find_element(*self.CARD_NUMBER_BUTTON).click()

    def add_card_number(self):
        self.driver.find_element(*self.ADD_CARD_NUMBER).click()

    def click_card_number_button(self):
        self.driver.find_element(*self.CARD_NUMBER_BUTTON).click()

    def input_card_number(self, card_number):
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.CARD_NUMBER).text

    def input_card_code(self, card_code):
        self.driver.find_element(*self.CARD_CODE).send_keys(card_code)

    def get_card_code(self):
        return self.driver.find_element(*self.CARD_CODE).text

    def card_number_link_button(self):
        #self.driver.find_element(*self.CARD_NUMBER_LINK_BUTTON).display()
        self.driver.find_element(*self.CARD_NUMBER_LINK_BUTTON).click()

    def click_card_number_close_button(self):
        self.driver.find_element(*self.CARD_NUMBER_CLOSE_BUTTON).click()

    def card_number_close_button(self):
        return self.driver.find_element(*self.CARD_NUMBER_CLOSE_BUTTON).get_property('value')

    def input_message_for_driver(self, message_for_driver):
        self.driver.find_element(*self.MESSAGE_FOR_DRIVER).send_keys(message_for_driver)

    def get_message_for_driver(self):
        return self.driver.find_element(*self.MESSAGE_FOR_DRIVER).text

    def order_blanket_and_handkerchiefs(self):
        self.driver.find_element(*self.ORDER_BLANKET_AND_HANDKERCHIEFS).click()

    def get_order_blanket_and_handkerchiefs(self):
        #return self.driver.find_element(*self.ORDER_BLANKET_AND_HANDKERCHIEFS).get_property('checked')
        return self.driver.find_element(*self.ORDER_BLANKET_CHECKBOX).is_selected()

    def order_ice_cream_plus_button(self):
        self.driver.find_element(*self.ORDER_ICE_CREAM_PLUS_BUTTON).click()

    def click_order_ice_cream_plus_button(self, order_ice_cream_plus_button):
        return self.driver.find_element(*self.ORDER_ICE_CREAM_PLUS_BUTTON).click(2)

    def order_ice_cream_counter(self):
        order_ice_cream = 2
        for i in range(order_ice_cream):
            WebDriverWait(self.driver,5).until(EC.element_to_be_clickable(self.ORDER_ICE_CREAM_PLUS_BUTTON)).click()

    def get_order_ice_cream(self):
        #return self.driver.find_element(By.ID, "int('2')").get_property('value')
        counter_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.ORDER_ICE_CREAM_COUNTER))
        return counter_element.text

    def click_ordering_a_taxi_button(self):
        return self.driver.find_element(*self.ORDERING_A_TAXI_BUTTON).click()

    def ordering_a_taxi_car_search_modal(self):
        self.driver.find_element(*self.ORDERING_A_TAXI_CAR_SEARCH_MODAL).is_displayed()

    def get_ordering_a_taxi_car_search_modal(self):
        return self.driver.find_element(*self.ORDERING_A_TAXI_CAR_SEARCH_MODAL).is_displayed()
