# Call all modules and functions in the "driver.py" file
from driver import *

# The "test_addtoCart" function performs automatic checking for adding items to the cart
def test_addtoCart(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(12345)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

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

    table = driver.find_element(By.CLASS_NAME, "table")

    # Go through all the rows in the cart table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Go through each column in each row
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

    if len(columns) > 1:
        # Get product's name in cart
        product_name_in_cart = columns[2].text

        # Get product's quantity in cart
        product_qty_in_cart = columns[6].text

        if product_name == product_name_in_cart:
            assert product_qty_in_cart == 4


def test_remove_item(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(2)

    driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
    time.sleep(2)

    status = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").text
    assert "Add to cart" in status

def test_view_cart(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(5)

    assert "cart.html" in driver.current_url

def test_firstname_empty(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(2)

    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    driver.find_element(By.ID, "last-name").send_keys("dat")
    time.sleep(2)

    driver.find_element(By.ID, "postal-code").send_keys(123)
    time.sleep(2)

    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Error: First Name is required" in error_message

def test_lastname_empty(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(2)

    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    driver.find_element(By.ID, "first-name").send_keys("dat")
    time.sleep(2)

    driver.find_element(By.ID, "postal-code").send_keys(123)
    time.sleep(2)

    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Error: Last Name is required" in error_message

def test_postalcode_empty(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(2)

    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    driver.find_element(By.ID, "first-name").send_keys("dat")
    time.sleep(2)

    driver.find_element(By.ID, "last-name").send_keys("dat")
    time.sleep(2)

    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']").text
    assert "Error: Postal Code is required" in error_message

def test_checkout_process(driver):
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    driver.find_element(By.ID, "shopping_cart_container").click()
    time.sleep(2)

    driver.find_element(By.ID, "checkout").click()
    time.sleep(2)

    driver.find_element(By.ID, "first-name").send_keys("dat")
    time.sleep(2)

    driver.find_element(By.ID, "last-name").send_keys("dat")
    time.sleep(2)

    driver.find_element(By.ID, "postal-code").send_keys(123)
    
    driver.find_element(By.ID, "continue").click()
    time.sleep(2)

    driver.find_element(By.ID, "finish").click()
    time.sleep(2)
    
    assert "checkout-complete" in driver.current_url
    

    
