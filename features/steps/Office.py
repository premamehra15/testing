import logging
import allure
from allure_commons.types import AttachmentType
from behave import *
from robot.utils import asserts
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from resources.testdata import *


class OfficePage:
    office = "//a[@id='office']"
    start_office_challenge = "//button[@id='start']"
    office_qn_one = "//p[@id='office_question_1']"
    office_ans_one = "//a[@id='office_answer_1']"
    pop_up_text = "//*[contains(text(),'%s')]"
    check_final_score = "//button[@id='leaderboard_link']"

    def __init__(self, driver):
        self.driver = driver

    @then('start the office challenge')
    def bus_challenge_funct(self):
        try:
            logging.info('Taking bus')
            WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, OfficePage.office))).click()

            logging.info('Start bus challenge')
            WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, OfficePage.start_office_challenge))).click()
        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
            asserts.fail(str(e))

    @then('answer office challenge question')
    def bus_challenge_quest(self):
        try:
            logging.info('Answering first question')
            office_first_qn = WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, OfficePage.office_qn_one)))
            if office_first_qn.is_displayed():
                WebDriverWait(
                    self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, OfficePage.office_ans_one))).click()
                logging.info('Verifying pop up')
                for info in info_pop_up:
                    pop_up_element = WebDriverWait(
                        self.driver, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, OfficePage.pop_up_text % info)))
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

