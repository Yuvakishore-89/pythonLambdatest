import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

username = os.getenv("yuvakishore2518")  # Replace the username
access_key = os.getenv("R0LLqY85PY6QMotKYVwBl3ql9oBssESGGeIBLYFEKFcyun5Pru")


class FirstSampleTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            'LT:Options': {
                "username": "yuvakishore2518",
                "accessKey": "R0LLqY85PY6QMotKYVwBl3ql9oBssESGGeIBLYFEKFcyun5Pru",
                "video": True,
                "platformName": "Windows 10",
                "resolution": "1920x1080",
                "network": True,
                "build": "Scenarios",
                "project": "Untitled",
                "name": "Test1",
                "console": "true",
                "seleium_version": "4.0.0",
                "driver_version": "105.0",
                "w3c": True,
                "plugin": "python-pytest"
            },
            "browserName": "Chrome",
            "browserVersion": "105.0",
        }
        self.driver = webdriver.Remote(
            command_executor="https://yuvakishore2518:R0LLqY85PY6QMotKYVwBl3ql9oBssESGGeIBLYFEKFcyun5Pru@hub.lambdatest.com/wd/hub".format(
                username, access_key),
            desired_capabilities=desired_caps)

        # tearDown runs after each test case

    def tearDown(self):
        self.driver.quit()

        # """ You can write the test cases here """
    def test_demo_site(self):
            # try:
        driver = self.driver
        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
        driver.set_window_size(1920, 1080)

            # Url
        print('Loading URL')
        driver.get("https://www.lambdatest.com/selenium-playground")

        driver.find_element(By.LINK_TEXT, "Drag & Drop Sliders").click()


        variable = driver.find_element(By.XPATH,"//*[@id='slider3']/div/input" )
        ActionChains(driver).drag_and_drop_by_offset(variable,120, 0).perform()

        slider = driver.find_element(By.XPATH,"//*[@id='rangeSuccess']").text
        assert "95" in slider

if __name__ == "__main__":
    unittest.main()
