import unittest
import time
import pyautogui as pya
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

username = ''  # use valid test login email
password = ''  # use valid test password
invalidUsername = 'unkownuserxyz@somedomain.com'  # use invalid test login
invalidPassword = '1nVal1dP@ssw0rd'  # use invalid test password
driver = webdriver.Chrome(executable_path="c:\webdrivers\chromedriver.exe")


class LoginScenarios(unittest.TestCase):
    def test_successful_login(self):
        driver.get("http://hudl.com")
        driver.implicitly_wait(1500)
        driver.find_element(By.CSS_SELECTOR,
                            'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary').click()
        assert "/login" in driver.current_url
        email = driver.find_element(By.ID, 'email').click()
        pya.typewrite(username)
        pw = driver.find_element(By.ID, 'password').click()
        pya.typewrite(password)
        driver.find_element(By.ID, 'logIn').click()
        time.sleep(3)  # Need to find a better way to wait until page loads
        assert '/home' in driver.current_url
        assert 'Home - Hudl' in driver.title
        driver.find_element(By.CLASS_NAME, 'hui-globaluseritem__avatar'), NoSuchElementException
        self.tearDown()


    def test_invalid_username(self):
        driver.get("http://hudl.com")
        driver.implicitly_wait(1500)
        driver.find_element(By.CSS_SELECTOR,
                            'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary').click()
        assert "/login" in driver.current_url
        email = driver.find_element(By.ID, 'email').click()
        pya.typewrite(invalidUsername)
        pw = driver.find_element(By.ID, 'password').click()
        pya.typewrite(password)
        driver.find_element(By.ID, 'logIn').click()
        time.sleep(3)  # Need to find a better way to wait until page loads
        assert '/login' in driver.current_url
        assert 'Log In - Hudl' in driver.title
        driver.find_element(By.CLASS_NAME, 'login-error-container'), NoSuchElementException
        self.tearDown()


    def test_invalid_password(self):
        driver.get("http://hudl.com")
        driver.implicitly_wait(1500)
        driver.find_element(By.CSS_SELECTOR,
                            'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary').click()
        assert "/login" in driver.current_url
        email = driver.find_element(By.ID, 'email').click()
        pya.typewrite(username)
        pw = driver.find_element(By.ID, 'password').click()
        pya.typewrite(invalidPassword)
        driver.find_element(By.ID, 'logIn').click()
        time.sleep(3)  # Need to find a better way to wait until page loads
        assert '/login' in driver.current_url
        assert 'Log In - Hudl' in driver.title
        driver.find_element(By.CLASS_NAME, 'login-error-container'), NoSuchElementException
        self.tearDown()


if __name__ == '__main__':
    unittest.main()
