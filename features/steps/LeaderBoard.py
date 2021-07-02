import logging
import allure
from allure_commons.types import AttachmentType
from behave import *
from robot.utils import asserts
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from resources.testdata import *


class LB:
    score_board = '//body/div[@class="row"]/div[@class="col-lg-12"]/p[@id="showData"]//td[contains(text(),' \
                  '"%s")]/following-sibling::td[contains(text(),"100")] '
    check_final_score = "//button[@id='leaderboard_link']",
    lead_board = '//*[contains(text(),"%s")]'

    def __init__(self, driver):
        self.driver = driver

    @then('check your score')
    def score_check(self):
        try:
            logging.info('Checking the score for the user')
            score_element = WebDriverWait(
                self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, LB.score_board % username)))
            if score_element.is_displayed:
                pass
            else:
                asserts.fail('The score is not available on the leader board')
            logging.info('Checking the leaderboard info')
            for info in leader_board:
                lead_board_element = WebDriverWait(
                    self.driver, 10).until(
                    EC.presence_of_element_located(
                        (By.XPATH, LB.lead_board % info)))
                if lead_board_element.is_displayed:
                    pass
                else:
                    asserts.fail('The info is not available on the leader board')

        except Exception as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot",
                          attachment_type=AttachmentType.PNG)
            asserts.fail(str(e))
