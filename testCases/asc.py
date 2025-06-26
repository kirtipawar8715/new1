import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://automation.credence.in/login")
driver.maximize_window()
#driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)

if driver.title == "CredKart":
    print("you are landed on correct page and it's title is:", driver.title)
    # Field - Email
    email_field = driver.find_element(By.ID, "email")
    email_field.send_keys(f"Credencejune01@credence.in")

    # Field - Password
    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("Credence@123")

    # Button - Login Now
    login_now_button = driver.find_element(By.CLASS_NAME, "btn")
    login_now_button.click()

    # Verify the User login Successfully
    wait = WebDriverWait(driver, 5)
    try :
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
        driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        print("User login Successfully")
        #driver.save_screenshot("User login Successfully.png")
    ##############################################################################
        ## Select Product
        driver.find_element(By.XPATH,"//h3[normalize-space()='Apple Macbook Pro']").click()
        # Add to Cart


       # Select Quantity
        #time.sleep(2)
        wait.until(
            expected_conditions.visibility_of_element_located((By.XPATH, "//select[@class='quantity']"))
            )
        quantity = Select(driver.find_element(By.XPATH,"//select[@class='quantity']"))
        quantity.select_by_visible_text("4")

        time.sleep(1)
        # proceed to checkout

        proceed_checkout = driver.find_element(By.CSS_SELECTOR,".btn.btn-success.btn-lg")
        proceed_checkout.click()


        # First Name
        driver.find_element(By.XPATH,"//input[@id='first_name']").send_keys("credence")

        # Last Name
        driver.find_element(By.XPATH,"//input[@id='last_name']").send_keys("june")


        # Mobile Number
        driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9876543210")

        # Address
        driver.find_element(By.XPATH,"//textarea[@id='address']").send_keys("Dhankawadi, Pune, MH, INDIA")

        # Zip
        driver.find_element(By.XPATH,"//input[@id='zip']").send_keys("411413")

        # State
        state = Select(driver.find_element(By.XPATH,"//select[@id='state']"))
        state.select_by_visible_text("Pune")


        # Owner Name
        driver.find_element(By.XPATH,"//input[@id='owner']").send_keys("credence june")

        # Cvv
        driver.find_element(By.XPATH,"//input[@id='cvv']").send_keys("257")

        time.sleep(1)
        # Card Number
        driver.find_element(By.XPATH,"//input[@id='cardNumber']").send_keys("4716")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("1089")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("9971")
        driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6531")

        time.sleep(1)
        # Month
        month = Select(driver.find_element(By.XPATH,"//select[@id='exp_month']"))
        month.select_by_visible_text("May")

        # Year
        year = Select(driver.find_element(By.XPATH,"//select[@id='exp_year']"))
        year.select_by_visible_text("2024")

        # Click on Checkout
        driver.find_element(By.XPATH,"//button[@id='confirm-purchase']").click()

        # Success Message
        wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//p[@class='w-lg-50 mx-auto']")))
        message = driver.find_element(By.XPATH, "//p[@class='w-lg-50 mx-auto']").text
        print(message)
        if "order number" in message:
            print("Order Placed Successfully")
            driver.save_screenshot("Order Placed Successfully.png")
        else:
            print("Order Placed Failed")

    except (NoSuchElementException, TimeoutError) as err:
        print(f"User login Failed,{err} ")
        driver.save_screenshot("User login Failed.png")
else:
    print("you are landed on wrong page and it's title is:", driver.title)


driver.quit()


