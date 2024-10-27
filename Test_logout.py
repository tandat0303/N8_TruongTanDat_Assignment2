from driver import *

def test_logout(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(12345)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Logout']").click()
    time.sleep(2)

    assert "http://localhost/eCommerceSite-PHP/login.php" in driver.current_url