import pytest
from selenium import webdriver



# class Testpytest():
driver = None
@pytest.fixture(autouse=True, scope='session')
def test_setup_close():
    global driver
    print("\nStart of setup")
    driver = webdriver.Firefox()
    print("\nEnd of setup")
    yield
    print("start of Yeild")
    driver.close()


def test_open_website():
    print("Start of open website")
    driver.get("http://testing-ground.scraping.pro/login")
    # self.assertIn("Web Scraper Testing Ground", self.driver.title)
    assert "Web Scraper Testing Ground" in driver.title
    print("End of Open website")
