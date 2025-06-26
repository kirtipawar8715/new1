import allure
import pytest
from faker import Faker

from pageObjects.registration_Page import RegistrationPage_Class
from utitlties.Logger import LoggerClass
from utitlties.readconfigfile import ReadConfig


@pytest.mark.usefixtures("setup")
class Test_Registration_002:
    log = LoggerClass.get_loggen()
    register_url = ReadConfig.get_registration_url()
    driver = None

    @pytest.mark.smoke
    @pytest.mark.regression
    #@pytest.mark.depends("test_verify_title_001") # here we have created the dependency # but this wont work when you are running the testcases parallel
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    @allure.title("test_registration_002")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Verify that user is able to register to the application")
    def test_registration_002(self):
        self.log.info("test_registration_002 is started")
        self.log.info(f"Opening the registration page-->{self.register_url}")
        self.driver.get(self.register_url)
        self.rp = RegistrationPage_Class(self.driver)
        random_name = Faker().first_name()
        random_email = Faker().email()
        self.log.info(f"Enter name-->{random_name}")
        self.rp.Enter_name(random_name)
        self.log.info(f"Enter email-->{random_email}")
        self.rp.Enter_email(random_email)
        self.log.info("Enter password")
        self.rp.Enter_password("Credencetest@123")
        self.log.info("Enter confirm password")
        self.rp.Enter_confirm_password("Credencetest@123")
        self.log.info("Click register button")
        self.rp.Click_register()
        self.log.info("Verify registration")
        if self.rp.Verify_menu() == "pass":
            self.log.info("test_registration_002 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_registration_002_pass.png")
            self.log.info("Click menu button")
            self.rp.Click_menu()
            self.log.info("Click logout button")
            self.rp.Click_logout()
            assert True
        else:
            self.log.info("test_registration_002 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_registration_002_fail.png")
            assert False
        self.log.info("test_registration_002 is completed")

