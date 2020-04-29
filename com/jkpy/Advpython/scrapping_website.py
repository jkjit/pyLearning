import pytest
from selenium import webdriver


class Testpytest():

    # @pytest.fixture(scope="session", autouse=True)
    # def setup(self):
    #     self.driver = webdriver.Firefox()
    #
    
    def test_open_website(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://testing-ground.scraping.pro/login")
        # self.assertIn("Web Scraper Testing Ground", self.driver.title)
        assert "Web Scraper Testing Ground" in self.driver.title
        self.driver.close()

    def test_correct_pwd(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://testing-ground.scraping.pro/login")
        user_element = self.driver.find_element_by_xpath("//*[@id=\"usr\"]")
        user_element.send_keys("admin")
        user_pwd = self.driver.find_element_by_xpath("//*[@id=\"pwd\"]")
        user_pwd.send_keys("12345")
        self.driver.find_element_by_xpath("//*[@id=\"case_login\"]/form/input[3]").click()
        assert "WELCOME" in self.driver.find_element_by_id("case_login").text
        self.driver.close()

    def test_incorrect_pwd(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://testing-ground.scraping.pro/login")
        user_element = self.driver.find_element_by_xpath("//*[@id=\"usr\"]")
        user_element.clear()
        user_pwd = self.driver.find_element_by_xpath("//*[@id=\"pwd\"]")
        user_pwd.clear()
        self.driver.find_element_by_xpath("//*[@id=\"case_login\"]/form/input[3]").click()
        assert "WELCOME" not in self.driver.find_element_by_id("case_login").text
        self.driver.close()

    def tear_down(self):
        self.driver.close()


if __name__ == '__main__':
    main()
