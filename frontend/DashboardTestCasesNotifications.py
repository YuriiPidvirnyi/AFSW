import unittest

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page import *


class NotificationTest(unittest.TestCase):
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

    def test_01_verify_that_notification_bell_icon_exists_and_clickable(self):
        self.login_page.login("Administrator")
        self.assertTrue(self.library_page.check_page_loaded())
        self.library_page.click_on_logo()
        self.bell = self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_BELL)
        self.assertTrue(self.bell)
        self.bell.click()
        time.sleep(0.5)
        self.assertTrue(self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP))

    def test_02_verify_notification_popup(self):
        self.assertTrue(self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP))
        self.assertTrue(self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP_NOTIFICATIONS_TITLE))
        self.assertEqual("NOTIFICATIONS",
                         self.dashboard_page.find_element(
                             *BasePageLocators.NOTIFICATION_POPUP_NOTIFICATIONS_TITLE).text)
        self.mark_as_read = self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP_MARK_ALL_READ_LINK)
        self.assertTrue(self.mark_as_read)
        self.assertEqual("Mark all as Read",
                         self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP_MARK_ALL_READ_LINK).text)
        self.assertTrue(self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP_CLOSE_SIGN))

    def test_03_verify_that_notification_popup_closed_if_click_on_cross_sign(self):
        self.assertTrue(self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP))
        self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP_CLOSE_SIGN).click()
        self.assertFalse(self.is_element_present(*BasePageLocators.NOTIFICATION_POPUP))

    def test_04_verify_that_notification_popup_closed_if_click_outside(self):
        self.bell = self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_BELL)
        self.assertTrue(self.bell)
        self.bell.click()
        self.assertTrue(self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_POPUP))
        self.bell_act = self.dashboard_page.find_element(*BasePageLocators.NOTIFICATION_BELL_ACTIVE)
        self.assertTrue(self.bell)
        self.bell_act.click()
        self.assertFalse(self.is_element_present(*BasePageLocators.NOTIFICATION_POPUP))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):

        """
        Helper method to confirm the presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True


if __name__ == '__main__':
    unittest.main(verbosity=2)
