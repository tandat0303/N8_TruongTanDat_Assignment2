# Call all modules and functions in the "driver.py" file
from driver import *

# 
def test_checkout(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(12345)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    driver.find_element(By.XPATH, "//button[text()='Update Billing and Shipping Info']").click()
    time.sleep(2)

    if not is_billing_address_filled(driver):
        update_billing_address(driver)
        
    if not is_shipping_address_filled(driver):
        update_shipping_address(driver)

    driver.find_element(By.CLASS_NAME, "btn-primary").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Men").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Amazfit GTS 3 Smart Watch for Android iPhone").click()

    product_name = driver.find_element(By.CLASS_NAME, "p-title").text

    select_color = Select(driver.find_element(By.NAME, "color_id"))

    select_color.select_by_visible_text("Gray")
    time.sleep(2)

    qty_input = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty[name='p_qty']")
    qty_input.clear()
    qty_input.send_keys("4")
    
    driver.find_element(By.NAME, "form_add_to_cart").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@href='checkout.php']").click()
    time.sleep(2)

    select_payment_method = Select(driver.find_element(By.NAME, "payment_method"))
    select_payment_method.select_by_visible_text("Bank Deposit")
    time.sleep(2)

    driver.find_element(By.NAME, "transaction_info").send_keys("Please deliver it quickly and carefully!")
    time.sleep(2)

    driver.find_element(By.NAME, "form3").click()
    time.sleep(2)

    success_message = driver.find_element(By.CSS_SELECTOR, "h3").text

    assert "Congratulation! Payment is successful." in success_message


def update_billing_address(driver):
    driver.find_element(By.NAME, "cust_b_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_cname").send_keys("SGU")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_phone").send_keys("0383161867")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_b_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_address").send_keys("An Duong Vuong")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)
    
    driver.find_element(By.NAME, "cust_b_state").send_keys("Mien Nam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_b_zip").send_keys(112233)
    time.sleep(1.5)


def update_shipping_address(driver):
    driver.find_element(By.NAME, "cust_s_name").send_keys("Truong Tan Dat")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_cname").send_keys("SGU")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_phone").send_keys("0383161867")
    time.sleep(1.5)

    select_element = Select(driver.find_element(By.NAME, "cust_s_country"))

    select_element.select_by_visible_text("Vietnam")
    time.sleep(1,5)

    driver.find_element(By.NAME, "cust_s_address").send_keys("112 Huynh Ba Chanh")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_city").send_keys("Ho Chi Minh")
    time.sleep(1.5)
    
    driver.find_element(By.NAME, "cust_s_state").send_keys("Mien Nam")
    time.sleep(1.5)

    driver.find_element(By.NAME, "cust_s_zip").send_keys(112233)
    time.sleep(1.5)


def is_billing_address_filled(driver):
    required_fields = ["cust_b_name", "cust_b_cname", "cust_b_phone", "cust_b_address", "cust_b_city", "cust_b_state", "cust_b_zip"]
    for field_name in required_fields:
        field_value = driver.find_element(By.NAME, field_name).get_attribute("value")
        if not field_value:
            return False
    return True


def is_shipping_address_filled(driver):
    required_fields = ["cust_s_name", "cust_s_cname", "cust_s_phone", "cust_s_address", "cust_s_city", "cust_s_state", "cust_s_zip"]
    for field_name in required_fields:
        field_value = driver.find_element(By.NAME, field_name).get_attribute("value")
        if not field_value:
            return False
    return True