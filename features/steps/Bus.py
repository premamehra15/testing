import logging
import allure
from allure_commons.types import AttachmentType
from behave import *
from robot.utils import asserts
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from resources.testdata import *


class BusPage:
    bus = "//a[@id='bus']"
    start_bus_challenge = "//button[@id='bus_timer_start']"
    bus_qn_one = "//p[@id='bus_question_1']"
    bus_ans_one = "//a[@id='bus_answer_1']"
    pop_up_text = "//*[contains(text(),'%s')]"
    check_final_score = "//button[@id='leaderboard_link']"

    def __init__(self, driver):
        self.driver = driver

    @then('start the bus challenge')
    def bus_challenge_funct(self):
        try:
            logging.info('Taking bus')
            WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, BusPage.bus))).click()

            logging.info('Start bus challenge')
            WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, BusPage.start_bus_challenge))).click()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
            asserts.fail(str(e))

    @then('answer bus challenge question')
    def bus_challenge_quest(self):
        try:
            logging.info('Answering first question')
            first_qn = WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, BusPage.bus_qn_one)))
            if first_qn.is_displayed():
                WebDriverWait(
                    self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, BusPage.bus_ans_one))).click()
                for info in info_pop_up:
                    pop_up_element = WebDriverWait(
                        self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, BusPage.pop_up_text % info)))
                    if pop_up_element.is_displayed:
                        pass
                    else:
                        asserts.fail('The info is not available')
            else:
                asserts.fail('Question not available')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
            asserts.fail(str(e))

    @then('go to leaderboard page')
    def leaderboard_link(self):
        try:
            logging.info('Checking score')
            final_score_element=WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, BusPage.check_final_score)))
            self.driver.execute_script("arguments[0].click();", final_score_element)
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
            asserts.fail(str(e))
