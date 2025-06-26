import allure
import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pageObjects.Login_Page import LoginPage_Class
from utitlties.Logger import LoggerClass
from utitlties.readconfigfile import ReadConfig


@pytest.mark.usefixtures("setup")
class Test_Login_001:
    log = LoggerClass.get_loggen()
    login_url = ReadConfig.get_login_url()
    driver = None
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    @pytest.mark.smoke
    @pytest.mark.regression
    #@pytest.mark.depends("test_verify_title_001") # here we have created the dependency # but this wont work when you are running the testcases parallel
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Verify that user is able to login to the application")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("test_verify_title_001")
    def test_verify_title_001(self):
        self.log.info("test_verify_title_001 is started")
        self.log.info(f"Opening the login page-->{self.login_url}")
        self.driver.get(self.login_url)
        self.log.info("verifying page title")
        self.log.info(f"Title of the page-->{self.driver.title}")
        if self.driver.title == "CredKart":
            self.log.info("test_verify_title_001 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_title_001_pass.png")
            assert True
        else:
            self.log.info("test_verify_title_001 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_title_001_fail.png")
            assert False
        self.log.info("test_verify_title_001 is completed")


    @pytest.mark.smoke
    @pytest.mark.regression
    #@pytest.mark.dependency(depends=["test_verify_title_001"]) # here we have used the dependency
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.title("test_verify_login_002")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that user is able to login to the application")
    def test_verify_login_002(self):
        self.log.info("test_verify_login_002 is started")
        self.log.info(f"Opening the login page-->{self.login_url}")
        self.driver.get(self.login_url)
        self.lp = LoginPage_Class(self.driver)
        self.log.info("Enter email")
        self.lp.Enter_email(self.email)
        self.log.info("Enter password")
        self.lp.Enter_password(self.password)
        self.log.info("Click login button")
        self.lp.Click_login()
        self.log.info("Verify login")
        if  self.lp.Verify_menu() == "pass":
            self.log.info("test_verify_login_002 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_login_002_pass.png")
            self.log.info("Click menu button")
            self.lp.Click_menu()
            self.log.info("Click logout button")
            self.lp.Click_logout()
            assert True
        else:
            self.log.info("test_verify_login_002 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_login_002_fail.png")
            assert False
        self.log.info("test_verify_login_002 is completed")



# command
# pytest -v -s -n auto --html=HTML_Reports/report.html --alluredir=allure-results