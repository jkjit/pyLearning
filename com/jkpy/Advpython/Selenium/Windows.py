import time

import pytest
from selenium import webdriver
import selenium.webdriver.support.wait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.actions import key_actions as ka
from selenium.webdriver.common.action_chains

ka.KeyActions.
kc.ActionChains

def test_open_website():
    print("Start of open website")
    driver = webdriver.Firefox()
    wait.WebDriverWait(driver,5,2,None)
    # set implicit time to 30 seconds

    # driver.implicitlyWait(30)
    # navigate to the url
    driver.get("https://chercher.tech/python/windows-selenium-python")
    # get the Session id of the Parent
    parentGUID = driver.current_window_handle
    # click the button to open new window
    print(f'Printing Parent ID: {parentGUID}')
    driver.find_element(By.ID("two-window")).click()
    # driver.find_element_by_id("two-window").click()
    # time.sleep(5000)
    # get the All the session id of the browsers
    allGUID = driver.window_handles
    # pint the title of th epage
    # print("Page title before Switching : " + driver.title())
    # print("Total Windows : " + len(allGUID))
    # iterate the values in the set
    print(allGUID)
    for guid in allGUID:
        # one enter into if blobk if the GUID is not equal to parent window's GUID
        print(f'inside FOr loop')
        if guid != parentGUID:
            # switch to the guid
            # driver.switch_to_window(guid);
            print(guid)
            driver.switch_to(guid)
        else:
            print(f'Am out of IF and inside Else')
            driver.switch_to_window(guid.title())
        # break the loop
        break
    # search on the google page
    driver.find_element_by_name("q").send_keys("success")
    # print the title after switching
    print("Page title after Switching to goolge : " + driver.title())
    # time.sleep(5000);
    # close the browser
    driver.execute_script("window.scrollTo")
    driver.close()
    # switch back to the parent window
    # driver.switch_to_window(parentGUID);
    driver.switch_to(parentGUID)
    # print the title
    print("Page title after switching back to Parent: " + driver.title())


test_open_website()