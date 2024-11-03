# Call all modules and functions in the "driver.py" file
from driver import *
import random
from selenium.common.exceptions import UnexpectedAlertPresentException

# Test the adding item section
def test_add_item(driver):
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

    # Using the "Select" module of Selenium to be able to use the select item in HTML
    select_color = Select(driver.find_element(By.NAME, "color_id"))

    # Use the "select_by_visible_text()" method to set the value for the select item
    select_color.select_by_visible_text("Gray")
    time.sleep(2)
    
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

        # # Get product's quantity in cart if you want to check the quantity
        # product_qty_in_cart = columns[6].text

        assert product_name == product_name_in_cart


# Test the removing item section
def test_remove_item(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    driver.find_element(By.LINK_TEXT, "Men").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Amazfit GTS 3 Smart Watch for Android iPhone").click()

    product_name = driver.find_element(By.CLASS_NAME, "p-title").text
    
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

        if product_name == product_name_in_cart:
            # Remove product if its name existed in cart
            driver.find_element(By.CLASS_NAME, "trash").click()
            time.sleep(2)
        
        assert product_name not in product_name_in_cart


# Test cart viewing
def test_view_cart(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    time.sleep(2)

    # Navigate to cart page to see all products that user had added
    assert "http://localhost/eCommerceSite-PHP/cart.php" in driver.current_url


# Test increase the quantity of product in cart
def test_increase_amount(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    driver.find_element(By.LINK_TEXT, "Men").click()
    time.sleep(2)

    driver.find_element(By.LINK_TEXT, "Amazfit GTS 3 Smart Watch for Android iPhone").click()
    
    driver.find_element(By.NAME, "form_add_to_cart").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    time.sleep(2)

    table = driver.find_element(By.CLASS_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")

    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

        if len(columns) > 7:
            qty_input = columns[6].find_element(By.NAME, "quantity[]")
            qty_input.clear()
            time.sleep(1)

            qty_input.send_keys("4")
            time.sleep(1)

            # Click "Update Cart"
            driver.find_element(By.NAME, "form1").click()
            time.sleep(2)

            # If there was an alert after updating, accept it
            try:
                alert = driver.switch_to.alert
                alert.accept()  # Accept alert
                time.sleep(2)
                break
            except UnexpectedAlertPresentException:
                print("There is no alert to be handle")
                break

    # Get the cart table and rows object
    table_new = driver.find_element(By.CLASS_NAME, "table")
    rows_new = table_new.find_elements(By.TAG_NAME, "tr")

    for row in rows_new:
        columns = row.find_elements(By.TAG_NAME, "td")

        if len(columns) > 7:
            qty = columns[6].find_element(By.NAME, "quantity[]").get_attribute("value")
            assert qty == "4" # Check if the updated quantity is the same as we have input


# Test add more than 1 product
def test_add_products(driver):
    driver.get('http://localhost/eCommerceSite-PHP/login.php')

    driver.find_element(By.NAME, "cust_email").send_keys("ls17189a3.11@gmail.com")
    time.sleep(2)

    driver.find_element(By.NAME, "cust_password").send_keys(123456)
    time.sleep(2)

    driver.find_element(By.NAME, "form1").click()

    driver.find_element(By.XPATH, "//a[contains(text(), 'Home')]").click()
    time.sleep(2)

    products = ["Men's Soft Classic Sneaker",
                "Truck Boys Pajamas Toddler Sleepwear Clothes",
                "Digital Infrared Thermometer for Adults and Kids"]
    
    quantities = []

    for product in products:
        driver.find_element(By.NAME, "search_text").send_keys(product)
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[text()='Search']").click()
        time.sleep(2)

        driver.find_element(By.LINK_TEXT, product).click()
        time.sleep(2)

        qty_input = driver.find_element(By.CSS_SELECTOR, "input.input-text.qty[name='p_qty']")
        qty_input.clear()

        qty = random.randint(1, 5)
        qty_input.send_keys(qty)
        time.sleep(2)

        quantities.append(int(qty))

        driver.find_element(By.NAME, "form_add_to_cart").click()
        time.sleep(2)

    driver.find_element(By.XPATH, "//a[contains(text(), 'Cart')]").click()
    time.sleep(2)

    table = driver.find_element(By.CLASS_NAME, "table")

    # Go through all the rows in the cart table
    rows = table.find_elements(By.TAG_NAME, "tr")

    product_in_cart = []
    quantity_in_cart = []

    # Go through each column in each row
    for row in rows:
        columns = row.find_elements(By.TAG_NAME, "td")

        if len(columns) > 7:
            product_name = columns[2].text # Get product name
            product_in_cart.append(product_name) # Add product name to the list

            product_quantity = columns[6].find_element(By.NAME, "quantity[]").get_attribute("value") # Get product quantity
            quantity_in_cart.append(int(product_quantity)) # Âdd product quantity to the list

    # Check if the products before being added to cart are the same the products in cart
    for product in product_in_cart:
        assert product in products
    
    for quantity in quantity_in_cart:
        assert quantity in quantities

            

        




    

    

    
