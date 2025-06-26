import pytest

from pageObjects.CheckOut_Page import Checkout_Class
from utitlties.Logger import LoggerClass
from utitlties.readconfigfile import ReadConfig


@pytest.mark.usefixtures("setup")
class Test_Checkout_003:
    log = LoggerClass.get_loggen()
    login_url = ReadConfig.get_login_url()
    driver = None
    email = ReadConfig.get_email()
    password = ReadConfig.get_password()

    def test_checkout_004(self):
        self.log.info("test_checkout_004 is started")
        self.log.info(f"Opening the login page-->{self.login_url}")
        self.driver.get(self.login_url)
        self.co = Checkout_Class(self.driver)
        self.log.info("Enter email")
        self.co.Enter_email(self.email)
        self.log.info("Enter password")
        self.co.Enter_password(self.password)
        self.log.info("Click login button")
        self.co.Click_login()
        self.log.info("Click product button")
        self.co.Click_product()
        self.log.info("Click add to cart button")
        self.co.Click_add_to_cart()
        self.log.info("Click proceed to checkout button")
        self.co.Click_proceed_to_checkout()
        self.log.info("Enter first name")
        self.co.Enter_first_name("Test")
        self.log.info("Enter last name")
        self.co.Enter_last_name("User")
        self.log.info("Enter phone number")
        self.co.Enter_phone("1234567890")
        self.log.info("Enter address")
        self.co.Enter_address("Test Address, Pune, maharashtra")
        self.log.info("Enter zip code")
        self.co.Enter_zip("411413")
        self.log.info("Select state")
        self.co.Select_state("Pune")
        self.log.info("Enter owner name")
        self.co.Enter_owner_name("Test User")
        self.log.info("Enter cvv")
        self.co.Enter_cvv("257")
        self.log.info("Enter card number")
        self.co.Enter_card_number("4716")
        self.co.Enter_card_number("1089")
        self.co.Enter_card_number("9971")
        self.co.Enter_card_number("6531")
        self.co.Select_year("2026")
        self.co.Select_month("May")
        self.log.info("Click continue checkout button")
        self.co.Click_continue_checkout()
        self.log.info("Verify checkout")
        if "order number" in self.co.Get_message():
            self.log.info("test_checkout_004 is passed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_checkout_004_pass.png")
            assert True
        else:
            self.log.info("test_checkout_004 is failed")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_checkout_004_fail.png")
            assert False
