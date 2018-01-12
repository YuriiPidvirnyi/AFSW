import unittest

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page import *


class InitialStateDashboardTest(unittest.TestCase):
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

    def test_01_verify_that_user_logged_in_as_admin(self):
        self.login_page.login("Administrator")
        self.assertTrue(self.library_page.check_page_loaded())
        # self.login_page.get_screen_shot("test_01_verify_logged_in_as_admin.png")

    def test_02_verify_that_dashboard_page_open(self):
        self.library_page.click_on_logo()
        self.assertTrue("http://localhost:8080/#/dashboard", self.dashboard_page.get_url())
        self.login_page.get_screen_shot("test_02_verify_that_dashboard_page_open.png")

    def test_03_verify_that_welcome_message_is_presented_and_correct(self):
        self.assertEqual(DashboardPageLocators.WELCOME_ADMIN_TEXT,
                         self.driver.find_element(*DashboardPageLocators.WELCOME).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.WELCOME_ADMIN_TEXT))

    def test_04_verify_that_dashboard_greet_is_presented_and_correct(self):
        self.assertEqual(DashboardPageLocators.DASHBOARD_GREET_TEXT,
                         self.driver.find_element(*DashboardPageLocators.DASHBOARD_GREET).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.DASHBOARD_GREET_TEXT))

    def test_05_verify_that_get_started_button_exists(self):
        self.assertEqual(DashboardPageLocators.GET_STARTED_BUTTON_TEXT,
                         self.driver.find_element(*DashboardPageLocators.GET_STARTED_BUTTON).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.GET_STARTED_BUTTON_TEXT))

    def test_06_verify_that_get_started_button_leads_to_library(self):
        self.driver.find_element(*DashboardPageLocators.GET_STARTED_BUTTON).click()
        self.assertTrue(self.library_page.check_page_loaded())
        self.library_page.click_on_logo()
        self.assertTrue(self.dashboard_page.check_page_loaded())

    def test_07_verify_that_recent_updates_widget_exists(self):
        self.assertEqual(DashboardPageLocators.RECENT_UPDATES_NAME,
                         self.driver.find_element(*DashboardPageLocators.RECENT_UPDATES).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.RECENT_UPDATES_NAME))

    def test_08_verify_that_shared_with_me_widget_exists(self):
        self.assertTrue(self.driver.find_element(*DashboardPageLocators.SHARED_WITH_ME))
        self.assertEqual(DashboardPageLocators.SHARED_WITH_ME_NAME,
                         self.driver.find_element(*DashboardPageLocators.SHARED_WITH_ME).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.SHARED_WITH_ME_NAME))

    def test_09_verify_that_activities_feed_widget_exists(self):
        self.assertEqual(DashboardPageLocators.ACTIVITIES_FEED_NAME,
                         self.driver.find_element(*DashboardPageLocators.ACTIVITIES_FEED).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.ACTIVITIES_FEED_NAME))

    def test_10_verify_that_documentation_tile_exists_and_correct(self):
        self.assertTrue(self.dashboard_page.find_element(*DashboardPageLocators.DOC_LINK))
        self.assertEqual(DashboardPageLocators.DOC_LINK_NAME,
                         self.driver.find_element(*DashboardPageLocators.DOC_LINK_NAME_LOC).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.DOC_LINK_NAME))
        self.assertEqual(DashboardPageLocators.DOC_LINK_TEXT,
                         self.driver.find_element(*DashboardPageLocators.DOC_LINK_TEXT_LOC).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.DOC_LINK_TEXT))

    def test_11_verify_that_video_tutorials_tile_exists_and_correct(self):
        self.assertTrue(self.dashboard_page.find_element(*DashboardPageLocators.VIDEO_LINK))
        self.assertEqual(DashboardPageLocators.VIDEO_LINK_NAME,
                         self.driver.find_element(*DashboardPageLocators.VIDEO_LINK_NAME_LOC).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.VIDEO_LINK_NAME))
        self.assertEqual(DashboardPageLocators.VIDEO_LINK_TEXT,
                         self.driver.find_element(*DashboardPageLocators.VIDEO_LINK_TEXT_LOC).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.VIDEO_LINK_TEXT))

    def test_12_verify_that_documentation_tile_leads_to_datawatch_docs(self):
        self.dashboard_page.find_element(*DashboardPageLocators.DOC_LINK).click()
        time.sleep(3)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.assertEqual(self.driver.current_url, DashboardPageLocators.DOC_LINK_URL)
        print("\n\tcriterion: {}".format(DashboardPageLocators.DOC_LINK_URL))
        self.assertEqual(self.driver.title, "Product Documentation - Datawatch Corporation")
        print("\n\tcriterion: {}".format("Product Documentation - Datawatch Corporation"))
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.CONTROL + 'w')
        self.driver.switch_to.window(handles[0])
        self.dashboard_page.check_page_loaded()
        time.sleep(1)

    def test_13_verify_that_video_tutorials_tile_leads_to_datawatch_youtube(self):
        self.dashboard_page.find_element(*DashboardPageLocators.VIDEO_LINK).click()
        time.sleep(3)
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[2])
        self.assertEqual(self.driver.current_url, DashboardPageLocators.VIDEO_LINK_URL)
        print("\n\tcriterion: {}".format(DashboardPageLocators.VIDEO_LINK_URL))
        self.title = self.driver.title
        self.assertEqual("Datawatch Monarch Swarm - YouTube - YouTube", self.title)
        print("\n\tcriterion: {}".format("Datawatch Monarch Swarm - YouTube - YouTube"))
        self.driver.switch_to.window(handles[0])
        self.dashboard_page.check_page_loaded()
        time.sleep(1)

    def test_14_verify_that_recent_updates_widget_placeholder_is_presented_and_correct(self):
        self.assertEqual(DashboardPageLocators.RECENT_UPDATES_PLACEHOLDER_TEXT,
                         self.driver.find_element(*DashboardPageLocators.RECENT_UPDATES_PLACEHOLDER).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.RECENT_UPDATES_PLACEHOLDER_TEXT))

    def test_15_verify_that_shared_with_me_widget_placeholder_is_presented_and_correct(self):
        self.assertEqual(DashboardPageLocators.SHARED_WITH_ME_PLACEHOLDER_TEXT,
                         self.driver.find_element(*DashboardPageLocators.SHARED_WITH_ME_PLACEHOLDER).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.SHARED_WITH_ME_PLACEHOLDER_TEXT))

    def test_16_verify_that_activities_feed_widget_placeholder_is_presented_and_correct(self):
        self.assertEqual(DashboardPageLocators.ACTIVITIES_FEED_PLACEHOLDER_TEXT,
                         self.driver.find_element(*DashboardPageLocators.ACTIVITIES_FEED_PLACEHOLDER).text)
        print("\n\tcriterion: {}".format(DashboardPageLocators.ACTIVITIES_FEED_PLACEHOLDER_TEXT))

    def test_17_verify_that_user_logged_out(self):
        self.dashboard_page.logout()
        self.assertTrue(self.login_page.check_page_loaded())
        self.login_page.get_screen_shot("test_14_verify_that_user_logged_out.png")

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
