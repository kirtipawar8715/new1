from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage_Class:

    text_email_id = "email"
    test_password_id = "password"
    button_login_Xpath = "//button[@type='submit']"
    menu_xpath = "//a[@role='button']"
    link_logout_xpath = "//a[normalize-space()='Logout']"


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)



    def Enter_email(self, email):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.text_email_id)))
        self.driver.find_element(By.ID, self.text_email_id).clear()
        self.driver.find_element(By.ID, self.text_email_id).send_keys(email)

    def Enter_password(self, password):
        self.wait.until(expected_conditions.presence_of_element_located((By.ID, self.test_password_id)))
        self.driver.find_element(By.ID, self.test_password_id).clear()
        self.driver.find_element(By.ID, self.test_password_id).send_keys(password)

    def Click_login(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.button_login_Xpath)))
        self.driver.find_element(By.XPATH, self.button_login_Xpath).click()

    def Click_menu(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.menu_xpath)))
        self.driver.find_element(By.XPATH, self.menu_xpath).click()

    def Click_logout(self):
        self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.link_logout_xpath)))
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def Verify_menu(self):
        try:
            self.wait.until(expected_conditions.presence_of_element_located((By.XPATH, self.menu_xpath)))
            return "pass"
        except:
            return "fail"











#1 Verify title
#2 Login
#3 registration
#4 Checkout
#5 Login_params
#6 Login_Excel