import pytest
from selenium import webdriver
from selenium.webdriver.firefox import firefox_profile

class website():
    # @pytest.fixture(scope="session", autouse=True)
    # def setup(self):
    #     self.driver = webdriver.Firefox()
    #     self.driver.get("http://testing-ground.scraping.pro/login")
    #
    driver = webdriver.Firefox()

    # @classmethod
    def test_open_website(cls):
        driver = cls.driver
        driver.get("http://testing-ground.scraping.pro/login")
        assert "Web Scraper Testing Ground" in driver.title
        # driver.close()

    @classmethod
    def test_correct_pwd(cls):
        driver = cls.driver
        driver.get("http://testing-ground.scraping.pro/login")
        user_element = driver.find_element_by_xpath("//*[@id=\"usr\"]")
        user_element.send_keys("admin")
        user_pwd = driver.find_element_by_xpath("//*[@id=\"pwd\"]")
        user_pwd.send_keys("12345")
        driver.find_element_by_xpath("//*[@id=\"case_login\"]/form/input[3]").click()
        assert "WELCOME" in driver.find_element_by_id("case_login").text
        # driver.close()

    @classmethod
    def test_incorrect_pwd(cls):
        driver = cls.driver
        driver.get("http://testing-ground.scraping.pro/login")
        user_element = driver.find_element_by_xpath("//*[@id=\"usr\"]")
        user_element.clear()
        user_pwd = driver.find_element_by_xpath("//*[@id=\"pwd\"]")
        user_pwd.clear()
        driver.find_element_by_xpath("//*[@id=\"case_login\"]/form/input[3]").click()
        assert "WELCOME" not in driver.find_element_by_id("case_login").text
        # driver.close()

    @classmethod
    def tear_down(cls):
        cls.driver.close()


# if __name__ == '__main__':
#     main()

web = website()
web.test_open_website()
web.test_correct_pwd()
web.test_incorrect_pwd()
web.tear_down()