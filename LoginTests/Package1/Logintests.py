import unittest
import time
import pyautogui as pya
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

username = ''  # Use valid login for successful test
password = ''  # Use valid password for successful test
invalidUsername = 'unkownuserxyz@somedomain.com'  # use invalid test login
invalidPassword = '1nVal1dP@ssw0rd'  # use invalid test password

# driver
driver = webdriver.Chrome(executable_path="c:\webdrivers\chromedriver.exe")


class LoginScenarios(unittest.TestCase):
    def _setUp(self):
        self.driver = driver
        self.driver.get('http://www.hudl.com')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.find_element(By.CSS_SELECTOR,
                                 'body > div.outer > header > div > a.mainnav__btn.mainnav__btn--primary').click()

    def _tearDown(self):
        self.driver.delete_all_cookies()
        self.driver.get("about:blank")

    def test_successful_login(self):
        self._setUp()
        assert "/login" in driver.current_url, 'Incorrect URL Found'
        email = driver.find_element(By.ID, 'email').click()
        pya.typewrite(username)
        pw = driver.find_element(By.ID, 'password').click()
        pya.typewrite(password)
        driver.find_element(By.XPATH, '/html/body/div[2]/form[1]/div[5]/div/label').click()
        driver.find_element(By.ID, 'logIn').click()
        time.sleep(3)  # Need to find a better way to wait until page loads
        assert '/home' in driver.current_url, 'Incorrect URL Found'
        assert 'Home - Hudl' in driver.title, 'Incorrect Page Title'
        driver.find_element(By.CLASS_NAME, 'hui-globaluseritem__avatar'), NoSuchElementException
        self._tearDown()

    def test_invalid_username(self):
        self._setUp()
        assert "/login" in driver.current_url, 'Incorrect URL Found'
        email = driver.find_element(By.ID, 'email').click()
        pya.typewrite(invalidUsername)
        pw = driver.find_element(By.ID, 'password').click()
        pya.typewrite(password)
        driver.find_element(By.ID, 'logIn').click()
        time.sleep(3)  # Need to find a better way to wait until page loads
        assert '/login' in driver.current_url, 'Incorrect URL Found'
        assert 'Log In - Hudl' in driver.title, 'Incorrect Page Title'
        driver.find_element(By.CLASS_NAME, 'login-error-container'), NoSuchElementException
        self._tearDown()

    def test_invalid_password(self):
        self._setUp()
        assert "/login" in driver.current_url, 'Incorrect URL Found'
        email = driver.find_element(By.ID, 'email').click()
        pya.typewrite(username)
        pw = driver.find_element(By.ID, 'password').click()
        pya.typewrite(invalidPassword)
        driver.find_element(By.ID, 'logIn').click()
        time.sleep(3)  # Need to find a better way to wait until page loads
        assert '/login' in driver.current_url, 'Incorrect URL Found'
        assert 'Log In - Hudl' in driver.title, 'Incorrect Page Title'
        driver.find_element(By.CLASS_NAME, 'login-error-container'), NoSuchElementException
        self._tearDown()

    def test_login_with_organization(self):  # Testing unable to log in with organization
        self._setUp()
        assert "/login" in driver.current_url, 'Incorrect URL Found'
        driver.find_element(By.ID, "logInWithOrganization").click()
        driver.find_element(By.ID, 'uniId_1').click()
        pya.typewrite(username)
        driver.find_element(By.XPATH, '/html/body/div/section/div/div/form/div[1]/button').click()
        assert '/login' in driver.current_url, 'Incorrect URL Found'
        assert driver.find_element(By.CLASS_NAME, 'login-error-container-code'), NoSuchElementException
        self._tearDown()


if __name__ == '__main__':
    unittest.main()
