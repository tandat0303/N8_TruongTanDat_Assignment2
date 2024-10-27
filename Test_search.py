from driver import *

def test_search_product(driver):
    driver.get("http://localhost/eCommerceSite-PHP/index.php")

    search_key = "shirt"
    
    driver.find_element(By.NAME, "search_text").send_keys(search_key)
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    time.sleep(2)

    product_titles = driver.find_elements(By.TAG_NAME, "h3")

    for title in product_titles:
        assert search_key.lower() in title.text.lower()



