# Call all modules and functions in the "driver.py" file
from driver import *

# Test the login functionality with valid email and password
def test_valid_login(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    assert "http://localhost/eCommerceSite-PHP/dashboard.php" in driver.current_url


# Test the login functionality with invalid email
def test_invalid_email(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Email Address does not match." in error


# Test the login functionality with invalid password
def test_invalid_password(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(1234)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Passwords do not match." in error


# Test the login functionality without filling the fields
def test_empty_fields(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "form1").click()

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Email and/or Password can not be empty." in error

