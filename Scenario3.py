import unittest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

        driver.find_element(By.LINK_TEXT, "Input Form Submit").click()

        driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()

        driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()
        message = driver.find_element(By.XPATH, "//input[@id='name']").get_attribute(name="validationMessage")
        print(message)
        assert "Please fill out this field." in message
        driver.find_element(By.NAME, "name").send_keys("Ram")

        driver.find_element(By.ID, "inputEmail4").send_keys("ram@example.com")

        driver.find_element(By.ID, "inputPassword4").send_keys("ram123")

        driver.find_element(By.ID, "company").send_keys("cisc")

        driver.find_element(By.ID,"websitename").send_keys("ci")

        country=Select(driver.find_element(By.NAME,"country"))
        country.select_by_visible_text("India")

        driver.find_element(By.ID, "inputCity").send_keys("mumbai")

        driver.find_element(By.ID,"inputAddress1").send_keys("xyz")

        driver.find_element(By.ID,"inputAddress2").send_keys("pqa")

        driver.find_element(By.ID,"inputState").send_keys("maha")

        driver.find_element(By.ID,"inputZip").send_keys("24151")

        driver.find_element(By.XPATH, "//*[@id='seleniumform']/div[6]/button").click()

        message1 = driver.find_element(By.XPATH,"//*[@id='__next']/div/section[3]/div/div/div[2]/div").text
        assert "Thanks for contacting us, we will get back to you shortly." in message1
        print("Message is correct")
if __name__ == "__main__":
    unittest.main()