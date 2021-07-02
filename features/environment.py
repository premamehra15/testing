from behave import *
from selenium import webdriver
from resources.testdata import *


@fixture
def use_browser(context, feature):
    if 'chrome' in feature.tags:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--incognito')
        context.driver = webdriver.Chrome(executable_path="Provide the path here", chrome_options=chrome_options)

    elif 'firefox' in feature.tags:
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--incognito")
        context.driver = webdriver.Firefox()

    context.driver.get(app_url)
    yield context.driver
    context.driver.quit()


def before_feature(context, feature):
    use_fixture(use_browser, context, feature)
