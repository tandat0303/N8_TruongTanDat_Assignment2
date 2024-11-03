# Call all modules and functions in the "driver.py" file
from driver import *

# Test the search functionality with valid keyword
def test_search_found(driver):
    driver.get("http://localhost/eCommerceSite-PHP/index.php")

    search_key = "shirt"
    
    driver.find_element(By.NAME, "search_text").send_keys(search_key)
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    time.sleep(2)

    # Finding all products whose title contain the keyword
    product_titles = driver.find_elements(By.TAG_NAME, "h3")

    for title in product_titles:
        assert search_key.lower() in title.text.lower()


# Test the search functionality with notfound keyword
def test_search_notfound(driver):
    driver.get("http://localhost/eCommerceSite-PHP/index.php")

    search_key = "agz"
    
    driver.find_element(By.NAME, "search_text").send_keys(search_key)
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    time.sleep(2)

    # Find the label "No result found"
    notfound_label = driver.find_element(By.TAG_NAME, "span").text

    assert "No result found" in notfound_label


# Test the search functionality with space keyword
def test_search_spaceKW(driver):
    driver.get("http://localhost/eCommerceSite-PHP/index.php")

    search_key = " "
    
    driver.find_element(By.NAME, "search_text").send_keys(search_key)
    time.sleep(2)

    driver.find_element(By.XPATH, "//button[text()='Search']").click()
    time.sleep(2)

    # The website show all products when the user search space keyword
    assert "search_text=+" in driver.current_url

