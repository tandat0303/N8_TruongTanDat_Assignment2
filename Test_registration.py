from driver import *

def test_registration(driver):
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

    assert "http://localhost/eCommerceSite-PHP/registration.php" in driver.current_url