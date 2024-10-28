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

        # Check if the product in the cart is the same as the product name before adding to the cart
        if product_name == product_name_in_cart:
            # Check if the quantity of the added product is the same as when entered
            assert product_qty_in_cart == 4
    

    
