from selenium import webdriver

# class Testpytest():

# @pytest.fixture(scope="session", autouse=True)
# def setup(self):
#     self.driver = webdriver.Firefox()
#     self.driver.get("http://testing-ground.scraping.pro/login")
#
driver = webdriver.Firefox()
url = "http://testing-ground.scraping.pro/login"


def test_open_website():
    driver.get(url)
    driver.maximize_window()
    assert "Web Scraper Testing Ground" in driver.title
    # driver.close()


def test_correct_pwd():
    driver.get(url)

    driver.maximize_window()
    user_element = driver.find_element_by_xpath("//*[@id=\"usr\"]")
    user_element.send_keys("admin")
    user_pwd = driver.find_element_by_xpath("//*[@id=\"pwd\"]")
    user_pwd.send_keys("12345")
    driver.find_element_by_xpath("//*[@id=\"case_login\"]/form/input[3]").click()
    assert "WELCOME" in driver.find_element_by_id("case_login").text



# if __name__ == '__main__':
#     main()

test_open_website()
test_correct_pwd()
