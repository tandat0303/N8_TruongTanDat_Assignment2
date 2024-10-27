from driver import *

def test_navigation(driver):
    driver.get("http://localhost/eCommerceSite-PHP/index.php")
    time.sleep(2)

    assert "Ecommerce PHP" in driver.title


    driver.find_element(By.LINK_TEXT, "About Us").click()
    time.sleep(2)

    assert "Ecommerce PHP - About Us" in driver.title


    driver.find_element(By.LINK_TEXT, "FAQ").click()
    time.sleep(2)

    assert "Fashionys.com - FAQ" in driver.title


    driver.find_element(By.LINK_TEXT, "Contact Us").click()
    time.sleep(2)

    assert "Fashionys.com - Contact" in driver.title


    driver.back()
    time.sleep(2)

    assert "Fashionys.com - FAQ" in driver.title


    driver.find_element(By.LINK_TEXT, "Home").click()
    time.sleep(2)

    assert "Ecommerce PHP" in driver.title



