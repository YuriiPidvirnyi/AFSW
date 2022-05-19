import unittest

import time

import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators import *

from page import *


class UserManagementTest(unittest.TestCase):
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
        # cls.dashboard_page = DashboardBasePage(cls.driver)
        cls.library_page = LibraryBasePage(cls.driver)

    def test_01_verify_that_user_management_page_open(self):
        login = self.driver.find_element_by_name("login")
        password = self.driver.find_element_by_name("password")
        login.send_keys(get_user("Administrator")["login"])
        password.send_keys(get_user("Administrator")["password"], Keys.ENTER)
        self.user_management_tab = self.driver.find_element_by_link_text("User Management")
        self.assertTrue(self.user_management_tab)
        self.user_management_tab.click()

    def test_02_verify_that_admin_login_is_correctly_displayed(self):
        self.assertEqual(get_user("Administrator")["login"], self.driver.find_element_by_css_selector(
            "div.main-table__cell-name-textual-info-wrapper:nth-child(2) > p:nth-child(1) > span:nth-child(1)").text)

    def test_03_verify_that_admin_first_name_is_correctly_displayed(self):
        self.assertEqual(get_user("Administrator")["name"], self.driver.find_element_by_css_selector(
            "div.table__cell:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)").text)

    def test_04_verify_that_admin_last_name_is_correctly_displayed(self):
        self.assertEqual(get_user("Administrator")["surname"], self.driver.find_element_by_css_selector(
            "div.table__cell:nth-child(3) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)").text)

    def test_05_verify_that_add_new_user_button_exists(self):
        self.assertEqual("Add New User", self.driver.find_element_by_css_selector(".button").text)

    def test_06_verify_that_admin_can_add_new_user(self):
        self.driver.find_element_by_css_selector(".button").click()
        self.assertTrue("Add New User", self.driver.find_element_by_css_selector(".users-form-header__title").text)
        name = self.driver.find_element_by_name("firstName")
        name.send_keys(get_user("Domenick")["name"])
        surname = self.driver.find_element_by_name("lastName")
        surname.send_keys(get_user("Domenick")["surname"])
        login = self.driver.find_element_by_name("login")
        login.send_keys(get_user("Domenick")["login"])
        password = self.driver.find_element_by_name("password")
        password.send_keys(get_user("Domenick")["password"])
        email = self.driver.find_element_by_name("email")
        email.send_keys(get_user("Domenick")["email"])
        role = self.driver.find_element_by_name("rolesSelector")
        role.send_keys(get_user("Domenick")["role"])
        self.select_role = self.driver.find_element_by_css_selector(".selector-suggestions__item")
        self.assertEqual(get_user("Domenick")["role"], self.select_role.text)
        self.select_role.click()
        self.save = self.driver.find_element_by_css_selector("button.button:nth-child(1)")
        self.save.click()
        time.sleep(1)
        self.assertEqual("2 users",
                         self.driver.find_element_by_css_selector(".main-layout__footer > div:nth-child(1)").text)

    def test_07_verify_that_new_user_login_is_correctly_displayed(self):
        self.assertEqual(get_user("Domenick")["login"], self.driver.find_element_by_css_selector(
            "div.table__row:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > p:nth-child(1) > span:nth-child(1)").text)

    def test_08_verify_that_new_user_first_name_is_correctly_displayed(self):
        self.assertEqual(get_user("Domenick")["name"], self.driver.find_element_by_css_selector(
            "div.table__row:nth-child(2) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)").text)

    def test_09_verify_that_new_user_last_name_is_correctly_displayed(self):
        self.assertEqual(get_user("Domenick")["surname"], self.driver.find_element_by_css_selector(
            "div.table__row:nth-child(2) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > p:nth-child(1) > span:nth-child(1)").text)

    def test_10_verify_that_admin_can_logout(self):
        elem = self.driver.find_element_by_css_selector(".circle > div:nth-child(1) > span:nth-child(1)")
        self.assertTrue(elem)
        hover = ActionChains(self.driver).move_to_element(elem)
        hover.perform()
        logout = self.driver.find_element_by_css_selector("li.select-menu__item:nth-child(2)")
        logout.click()
        self.login_page_greeting = self.driver.find_element_by_class_name("login-form__title")
        self.assertEqual(LOGIN_PAGE_GREETING, self.login_page_greeting.text)

    def test_11_verify_that_new_user_can_login(self):
        login = self.driver.find_element_by_name("login")
        password = self.driver.find_element_by_name("password")
        login.send_keys(get_user("Domenick")["login"])
        password.send_keys(get_user("Domenick")["password"], Keys.ENTER)
        self.assertTrue(self.driver.find_element_by_css_selector(".top-menu__link--active"))

    def test_12_verify_that_new_workspace_for_admin_is_in_user_library(self):
        time.sleep(7)
        self.assertEqual(ADMIN_WORKSPACE,
                         self.driver.find_element_by_css_selector(".main-table__cell-name-name").text)

    def test_13_verify_that_two_users_are_shown_in_user_management(self):
        self.driver.find_element_by_link_text("User Management").click()
        time.sleep(1)
        self.assertEqual("2 users",
                         self.driver.find_element_by_css_selector(".main-layout__footer > div:nth-child(1)").text)

    def test_14_verify_that_notification_bell_icon_counter_displays_2(self):
        self.assertEqual("2",
                         self.driver.find_element_by_css_selector(".top-controls__count_unread-notifications").text)

    def test_15_verify_that_are_two_unread_liked_shared_notifications(self):
        self.notif_bell_unread = self.driver.find_element_by_css_selector(".top-controls__icon_unread-notifications")
        self.assertTrue(self.notif_bell_unread)
        self.notif_bell_unread.click()
        self.notif_items = self.driver.find_element_by_xpath(
            "/html/body/main/div/div/div[1]/header/div[3]/div[1]/div[2]/div/ul")
        self.all_notif_items = self.notif_items.find_elements_by_xpath("child::li")
        self.assertEqual(2, len(self.all_notif_items))
        self.notif_texts = sorted([", ".join(item.text.split("\n")[:-1]) for item in self.all_notif_items])
        self.assertEqual("ADMINISTRATOR ADMINISTRATOR, liked your workspace {}, AA".format(ADMIN_WORKSPACE),
                         self.notif_texts[0])
        self.assertEqual("ADMINISTRATOR ADMINISTRATOR, shared a workspace {} with you, AA".format(ADMIN_WORKSPACE),
                         self.notif_texts[1])

    def test_16_verify_that_user_can_mark_all_notifications_as_read(self):
        self.mark_all_read = self.driver.find_element_by_css_selector(
            ".notifications__title-container_mark-all-as-read")
        self.assertTrue(self.mark_all_read)
        self.assertTrue(self.driver.find_element_by_link_text("Mark all as Read"))
        self.mark_all_read.click()
        self.notif_items = self.driver.find_element_by_css_selector(
            "ul.notifications__items:nth-child(2)")
        self.assertFalse(self.notif_items.find_elements_by_css_selector(
            "li.notifications__item div.notifications__container.notifications__container_unread"))
        self.assertTrue(self.notif_items.find_elements_by_css_selector(
            "li.notifications__item div.notifications__container.notifications__container"))

    def test_17_verify_that_user_can_close_notification_menu(self):
        self.notif_cross_icon = self.driver.find_element_by_css_selector(".icon-ic_close_black")
        self.assertTrue(self.notif_cross_icon)
        self.notif_cross_icon.click()
        self.assertFalse(self.is_element_present(By.CSS_SELECTOR, ".notifications"))

    def test_18_verify_that_notification_bell_icon_counter_is_not_displayed(self):
        self.assertFalse(self.is_element_present(By.CSS_SELECTOR, ".top-controls__count_unread-notifications"))
        self.assertFalse(self.driver.find_element_by_css_selector(".top-controls__count").is_displayed())

    def test_19_verify_that_there_are_two_read_notifications(self):
        self.notif_bell = self.driver.find_element_by_css_selector(".top-controls__icon_notifications")
        self.assertTrue(self.notif_bell)
        self.notif_bell.click()
        self.notif_items = self.driver.find_element_by_xpath(
            "/html/body/main/div/div/div[1]/header/div[3]/div[1]/div[2]/div/ul")
        self.all_notif_items = self.notif_items.find_elements_by_xpath("child::li")
        self.assertEqual(2, len(self.all_notif_items))
        self.notif_texts = sorted([", ".join(item.text.split("\n")[:-1]) for item in self.all_notif_items])
        self.assertEqual("ADMINISTRATOR ADMINISTRATOR, liked your workspace {}, AA".format(ADMIN_WORKSPACE),
                         self.notif_texts[0])
        self.assertEqual("ADMINISTRATOR ADMINISTRATOR, shared a workspace {} with you, AA".format(ADMIN_WORKSPACE),
                         self.notif_texts[1])

    def test_20_verify_that_there_are_not_any_unread_notifications(self):
        time.sleep(5)
        self.notif_items = self.driver.find_element_by_xpath(
            "/html/body/main/div/div/div[1]/header/div[3]/div[1]/div[2]/div/ul")
        self.unread_notif_items = self.notif_items.find_elements_by_xpath(
            ".//li/div[@class='notifications__container notifications__container_unread']")
        self.unread_notif_texts = sorted([", ".join(item.text.split("\n")) for item in self.unread_notif_items])
        self.assertFalse(self.notif_items.find_elements_by_xpath(
            ".//li/div[@class='notifications__container notifications__container_unread']"),
            msg="\nThere are some unread notification messages: {}".format(self.unread_notif_texts))

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
