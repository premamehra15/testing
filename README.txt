# README #

Tools/Language:
Python/Selenium webdriver
Model: Page object
Reports:Allure
Framework: BDD(Behave)



#Steps to install the setup #

Install pip3*************************
cmd:install pip3

Install Python3************************
pip3 install python3
Install Selenium:
cmd:pip3 install selenium

Download browser drivers*****************
chrome driver: https://sites.google.com/a/chromium.org/chromedriver/downloads
Firefox driver:https://github.com/mozilla/geckodriver/releases
Add the path variable for chrome and firefox driver

Install Behave*************************
cmd:pip3 install behave

Install Allure Behave******************
cmd: pip3 install allure-behave

Commands to run the testcases:
behave --tags chrome -f allure_behave.formatter:AllureFormatter -o Reports -v -s features
or  behave --tags chrome  -v -s features

Command to check the report:
allure serve "PATH OF THE REPORTS FOLDER/Reports"



