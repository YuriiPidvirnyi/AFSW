import unittest

import time

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page import LoginBasePage, LibraryBasePage, DashboardBasePage, UserManagementBasePage
from locators import *


class InitialStateLogInTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # get the path of ChromeDriverServer
        # dir = os.path.dirname(__file__)
        # chrome_driver_path = dir + "\chromedriver.exe"

        # create a new Chrome session
        executable_path = os.path.join(os.path.abspath(os.curdir), "frontend\program_data\chromedriver.exe")
        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        cls.driver = webdriver.Chrome(
            executable_path=executable_path,
            chrome_options=chrome_options)
        cls.driver.implicitly_wait(1)
        # cls.driver.maximize_window()

        # create a new Firefox session
        # executable_path = os.path.join(os.path.abspath(os.curdir), "program_data\cgeckodriver.exe")
        # cls.driver = webdriver.Firefox(executable_path=executable_path)
        # cls.driver.implicitly_wait(15)
        # cls.driver.maximize_window()

        # navigate to the application login page
        cls.driver.get("http:/localhost:8080")

        cls.login_page = LoginBasePage(cls.driver)
        cls.dashboard_page = DashboardBasePage(cls.driver)
        cls.library_page = LibraryBasePage(cls.driver)
        cls.user_page = UserManagementBasePage(cls.driver)

    def test_01_verify_that_login_page_open(self):
        self.assertTrue(self.login_page.check_page_loaded())

    def test_02_get_swarm_build_info(self):
        swarm_build_info = self.login_page.get_swarm_build_info()
        self.assertTrue(swarm_build_info)
        print(swarm_build_info.text)
        # return swarm_build_info.text

    def test_03_verify_login_page_url(self):
        self.assertEqual("http://localhost:8080/#/login", self.login_page.get_url())
        print("\n\tcriterion: 'http://localhost:8080/#/login'")

    def test_04_verify_page_title(self):
        self.assertEqual(BasePageLocators.PAGE_TITLE, self.login_page.get_title())
        print("\n\tcriterion: {}".format(BasePageLocators.PAGE_TITLE))

    def test_05_verify_login_greeting(self):
        self.assertEqual(LoginPageLocators.LOGIN_PAGE_GREETING_TEXT,
                         self.login_page.find_element(*LoginPageLocators.LOGIN_PAGE_GREETING).text)
        print("\n\tcriterion: {}".format(LoginPageLocators.LOGIN_PAGE_GREETING_TEXT))

    def test_06_verify_logged_in_as_admin(self):
        self.login_page.login("Administrator")
        # self.assertTrue(self.dashboard_page.check_page_loaded())
        time.sleep(3)
        self.assertTrue(self.library_page.check_page_loaded())
        self.login_page.get_screen_shot("test_06_verify_logged_in_as_admin.png")

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
