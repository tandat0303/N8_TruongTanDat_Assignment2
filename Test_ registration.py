# Call all modules and functions in the "driver.py" file
from driver import *

# Test the registration functionality
def test_registration(driver):
    driver.get('http://localhost/eCommerceSite-PHP/registration.php')

    driver.find_element(By.NAME, "cust_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_cname").send_keys("Sai Gon University")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.12@gmail.com")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_phone").send_keys("0383161867")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_address").send_keys("112 Huynh Ba Chanh")
    time.sleep(1.5)

    # Using the "Select" module of Selenium to be able to use the select item in HTML
    select_element = Select(driver.find_element(By.NAME, "cust_country"))

    # Use the "select_by_visible_text()" method to set the value for the select item
    select_element.select_by_visible_text("Vietnam")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_state").send_keys("Sai Gon")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_zip").send_keys(11223344)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_re_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(1.5)

    success = driver.find_element(By.CLASS_NAME, "success").text

    assert "Your registration is completed. Please check your email address to follow the process to confirm your registration." in success


# Test the registration functionality with the email that has been registered before
def test_existed_email(driver):
    driver.get('http://localhost/eCommerceSite-PHP/registration.php')

    driver.find_element(By.NAME, "cust_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_cname").send_keys("Sai Gon University")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_phone").send_keys("0383161867")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_address").send_keys("112 Huynh Ba Chanh")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_state").send_keys("Sai Gon")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_zip").send_keys(11223344)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_re_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(1.5)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Email Address Already Exists." in error
        

# Test the registration functionality without filling some fields
def test_empty_fields(driver):
    driver.get('http://localhost/eCommerceSite-PHP/registration.php')

    driver.find_element(By.NAME, "cust_cname").send_keys("Sai Gon University")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_address").send_keys("112 Huynh Ba Chanh")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_country"))
    select_element.select_by_visible_text("Vietnam")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_state").send_keys("Sai Gon")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_zip").send_keys(11223344)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_re_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(1.5)

    error = driver.find_element(By.CLASS_NAME, "error")

    # Get list of errors from HTMl and separate base on "<br>" tag
    error_texts = [text.strip() for text in error.get_attribute('innerHTML').split("<br>") if text.strip()]

    # List of error clusters to check
    keywords_to_check = [
        "Customer Name can not be empty.",
        "Email Address can not be empty",
        "Phone Number can not be empty.",
    ]

    # Checking each keyword clusters in the list of error clusters
    for keyword in keywords_to_check:
        assert any(keyword in error_text for error_text in error_texts)


# Test entering the special character in the "Name" field
def test_special_character(driver):
    driver.get('http://localhost/eCommerceSite-PHP/registration.php')

    # Add some special character (such as @,!,: ...) in field "Name"
    driver.find_element(By.NAME, "cust_name").send_keys("Dat@!")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_cname").send_keys("Sai Gon University")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3@gmail.com")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_phone").send_keys("0383161867")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_address").send_keys("112 Huynh Ba Chanh")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_state").send_keys("Sai Gon")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_zip").send_keys(11223344)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_re_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(1.5)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Fullname is not contain special character(s)." in error


# Test the retype password if it matches the password
def test_retypePW_match(driver):
    driver.get('http://localhost/eCommerceSite-PHP/registration.php')

    driver.find_element(By.NAME, "cust_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_cname").send_keys("Sai Gon University")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.12@gmail.com")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_phone").send_keys("123")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_address").send_keys("112 Huynh Ba Chanh")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_city").send_keys("HCM")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_state").send_keys("Sai Gon")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_zip").send_keys(11223344)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_re_password").send_keys(123454)
    time.sleep(1.5)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(1.5)

    error = driver.find_element(By.CLASS_NAME, "error").text

    assert "Passwords do not match." in error


