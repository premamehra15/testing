import logging
import allure
from allure_commons.types import AttachmentType
from behave import *
from robot.utils import asserts
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from resources.testdata import *


class Login:
    username = "// input[ @ type = 'text']"
    create_warrior = "//a[@id='warrior']"
    start_journey = "//a[@id='start']"

    def __init__(self, driver):
        self.driver = driver

    @when('user successfully created')
    def login_portal(self):
        try:

            logging.info('Entering the username')
            WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Login.username))).send_keys(username)
        except Exception as e:
            asserts.fail(str(e))
        logging.info('Creating user')
        try:
            WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Login.create_warrior))).click()
        except Exception:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
            asserts.fail("could not create warrior")
        logging.info('Entering the game')
        try:
            WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, Login.start_journey))).click()
        except Exception as e:
            asserts.fail(str(e))
