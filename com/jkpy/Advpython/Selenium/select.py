from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName = "Chrome"
Options = webdriver.ChromeOptions()
Options.headless = True
if browserName == "Chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=Options)


driver.implicitly_wait(10)
driver.get("https://www.reddit.com")
# driver.get_screenshot_as_png()
# driver.get_screenshot_as_file('abc.png')

S = lambda X: driver.execute_script('return document.body.parentNode.scroll' + X)
driver.set_window_size(S('Width'), S('Height'))
driver.find_element_by_tag_name('body').screenshot('fullpage.png')

# driver.close()
