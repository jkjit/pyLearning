import pytest
from selenium import webdriver

class Testpytest():
    # driver = None
    @pytest.fixture(autouse=True, scope='session')
    def my_driver(self):
        print("\nStart of setup")
        self.driver = webdriver.Firefox()
        # return driver
        print("\nEnd of setup")
        yield
        print("start of Yeild")
        self.driver.close()

    def test_open_website(self):
        print("Start of open website")
        self.driver.get("http://testing-ground.scraping.pro/login")
        # self.assertIn("Web Scraper Testing Ground", self.driver.title)
        assert "Web Scraper Testing Ground" in self.driver.title
        print("End of Open website")

if __name__ == '__main__':
    main()
