import unittest

import time

import os
from pywinauto.application import Application
from pywinauto.keyboard import SendKeys

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from element import get_user, get_input_path_and_file
from page import LoginBasePage, LibraryBasePage, UserManagementBasePage, DashboardBasePage
from locators import *


class CreateUsersGroupsAndAddUsersToGroups(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # get the path of ChromeDriverServer
        # dir = os.path.dirname(__file__)
        # chrome_driver_path = dir + "\chromedriver.exe"

        # create a new Chrome session
        executable_path = os.path.join(os.path.abspath(os.curdir), "frontend\program_data\chromedriver.exe")
        print(executable_path)
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

    def test_01_log_in_as_admin(self):
        self.assertTrue(self.login_page.check_page_loaded())
        swarm_build_info = self.login_page.get_swarm_build_info()
        self.assertTrue(swarm_build_info)
        print(swarm_build_info.text)
        # return swarm_build_info.text
        self.assertEqual("http://localhost:8080/#/login", self.login_page.get_url())
        self.assertEqual(BasePageLocators.PAGE_TITLE, self.login_page.get_title())
        self.assertEqual(LoginPageLocators.LOGIN_PAGE_GREETING_TEXT,
                         self.login_page.find_element(*LoginPageLocators.LOGIN_PAGE_GREETING).text)
        # self.assertTrue(self.dashboard_page.check_page_loaded())
        self.login_page.login("Administrator")
        self.assertTrue(self.library_page.check_page_loaded())

    def test_02_as_admin_create_User1(self):
        self.user_page.find_element(*BasePageLocators.USER_MANAGEMENT_TAB).click()
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.assertTrue(UserManagementPageLocators.ADD_NEW_USER_BUTTON_TEXT,
                        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).text)
        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).click()
        name = self.user_page.find_element(*UserManagementPageLocators.FIRST_NAME)
        name.send_keys(get_user("User1")["name"])
        surname = self.user_page.find_element(*UserManagementPageLocators.LAST_NAME)
        surname.send_keys(get_user("User1")["surname"])
        login = self.user_page.find_element(*UserManagementPageLocators.LOGIN)
        login.send_keys(get_user("User1")["login"])
        password = self.user_page.find_element(*UserManagementPageLocators.PASSWORD)
        password.send_keys(get_user("User1")["password"])
        email = self.user_page.find_element(*UserManagementPageLocators.EMAIL)
        email.send_keys(get_user("User1")["email"])
        role = self.user_page.find_element(*UserManagementPageLocators.ROLE)
        role.send_keys(get_user("User1")["role"])
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.ROLE_SELECTOR)
        self.assertEqual(get_user("User1")["role"], self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()
        time.sleep(1)

    def test_03_verify_that_User1_is_created_and_correctly_displayed(self):
        time.sleep(3)
        self.assertEqual(get_user("User1")["login"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LOGIN_1).text)
        self.assertEqual(get_user("User1")["name"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_FIRST_NAME_1).text)
        self.assertEqual(get_user("User1")["surname"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LAST_NAME_1).text)
        self.assertEqual("2 users",
                         self.user_page.find_element(*UserManagementPageLocators.FOOTER).text)

    def test_04_as_admin_create_User4(self):
        self.user_page.find_element(*BasePageLocators.USER_MANAGEMENT_TAB).click()
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.assertTrue(UserManagementPageLocators.ADD_NEW_USER_BUTTON_TEXT,
                        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).text)
        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).click()
        name = self.user_page.find_element(*UserManagementPageLocators.FIRST_NAME)
        name.send_keys(get_user("User4")["name"])
        surname = self.user_page.find_element(*UserManagementPageLocators.LAST_NAME)
        surname.send_keys(get_user("User4")["surname"])
        login = self.user_page.find_element(*UserManagementPageLocators.LOGIN)
        login.send_keys(get_user("User4")["login"])
        password = self.user_page.find_element(*UserManagementPageLocators.PASSWORD)
        password.send_keys(get_user("User4")["password"])
        email = self.user_page.find_element(*UserManagementPageLocators.EMAIL)
        email.send_keys(get_user("User4")["email"])
        role = self.user_page.find_element(*UserManagementPageLocators.ROLE)
        role.send_keys(get_user("User4")["role"])
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.ROLE_SELECTOR)
        self.assertEqual(get_user("User4")["role"], self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()

    def test_05_verify_that_User4_is_created_and_correctly_displayed(self):
        self.assertEqual(get_user("User4")["login"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LOGIN_2).text)
        self.assertEqual(get_user("User4")["name"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_FIRST_NAME_2).text)
        self.assertEqual(get_user("User4")["surname"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LAST_NAME_2).text)
        self.assertEqual("3 users",
                         self.user_page.find_element(*UserManagementPageLocators.FOOTER).text)

    def test_06_as_admin_create_DBA_user_group(self):
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.user_page.find_element(*UserManagementPageLocators.GROUPS_TAB).click()
        self.assertTrue(UserManagementPageLocators.ADD_NEW_GROUP_BUTTON_TEXT,
                        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_GROUP_BUTTON).text)
        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_GROUP_BUTTON).click()
        group_name = self.user_page.find_element(*UserManagementPageLocators.NEW_GROUP_NAME)
        group_name.send_keys(UserManagementPageLocators.DBA_GROUP_NAME_TEXT)
        group_description = self.user_page.find_element(*UserManagementPageLocators.NEW_GROUP_DESCRIPTION)
        group_description.send_keys(UserManagementPageLocators.DBA_GROUP_DESCRIPTION_TEXT)
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_NEW_GROUP_BUTTON)
        self.save.click()

    def test_07_verify_that_DBA_group_is_created_and_correctly_displayed_0_users(self):
        time.sleep(1)
        self.assertEqual(UserManagementPageLocators.DBA_GROUP_NAME_TEXT, self.user_page.find_element(
            *UserManagementPageLocators.DBA_GROUP_TABLE_NAME).text)
        self.assertEqual(UserManagementPageLocators.DBA_GROUP_DESCRIPTION_TEXT, self.user_page.find_element(
            *UserManagementPageLocators.DBA_GROUP_TABLE_DESCRIPTION).text)
        self.assertEqual("0", self.user_page.find_element(*UserManagementPageLocators.DBA_GROUP_USERS_COUNT).text)

    def test_08_log_in_as_User1(self):
        self.user_page.logout()
        self.assertTrue(self.login_page.check_page_loaded())
        self.assertEqual("http://localhost:8080/#/login", self.login_page.get_url())
        self.assertEqual(BasePageLocators.PAGE_TITLE, self.login_page.get_title())
        self.assertEqual(LoginPageLocators.LOGIN_PAGE_GREETING_TEXT,
                         self.login_page.find_element(*LoginPageLocators.LOGIN_PAGE_GREETING).text)
        # self.assertTrue(self.dashboard_page.check_page_loaded())
        self.login_page.login("User1")
        self.assertTrue(self.library_page.check_page_loaded())

    def test_09_as_User1_create_User2(self):
        self.user_page.find_element(*BasePageLocators.USER_MANAGEMENT_TAB).click()
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.assertTrue(UserManagementPageLocators.ADD_NEW_USER_BUTTON_TEXT,
                        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).text)
        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).click()
        name = self.user_page.find_element(*UserManagementPageLocators.FIRST_NAME)
        name.send_keys(get_user("User2")["name"])
        surname = self.user_page.find_element(*UserManagementPageLocators.LAST_NAME)
        surname.send_keys(get_user("User2")["surname"])
        login = self.user_page.find_element(*UserManagementPageLocators.LOGIN)
        login.send_keys(get_user("User2")["login"])
        password = self.user_page.find_element(*UserManagementPageLocators.PASSWORD)
        password.send_keys(get_user("User2")["password"])
        email = self.user_page.find_element(*UserManagementPageLocators.EMAIL)
        email.send_keys(get_user("User2")["email"])
        role = self.user_page.find_element(*UserManagementPageLocators.ROLE)
        role.send_keys(get_user("User2")["role"])
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.ROLE_SELECTOR)
        self.assertEqual(get_user("User2")["role"], self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()

    def test_10_verify_that_User2_is_created_and_correctly_displayed(self):
        self.assertEqual(get_user("User2")["login"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LOGIN_2).text)
        self.assertEqual(get_user("User2")["name"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_FIRST_NAME_2).text)
        self.assertEqual(get_user("User2")["surname"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LAST_NAME_2).text)
        self.assertEqual("4 users",
                         self.user_page.find_element(*UserManagementPageLocators.FOOTER).text)

    def test_11_as_User1_create_User3(self):
        self.user_page.find_element(*BasePageLocators.USER_MANAGEMENT_TAB).click()
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.assertTrue(UserManagementPageLocators.ADD_NEW_USER_BUTTON_TEXT,
                        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).text)
        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).click()
        name = self.user_page.find_element(*UserManagementPageLocators.FIRST_NAME)
        name.send_keys(get_user("User3")["name"])
        surname = self.user_page.find_element(*UserManagementPageLocators.LAST_NAME)
        surname.send_keys(get_user("User3")["surname"])
        login = self.user_page.find_element(*UserManagementPageLocators.LOGIN)
        login.send_keys(get_user("User3")["login"])
        password = self.user_page.find_element(*UserManagementPageLocators.PASSWORD)
        password.send_keys(get_user("User3")["password"])
        email = self.user_page.find_element(*UserManagementPageLocators.EMAIL)
        email.send_keys(get_user("User3")["email"])
        role = self.user_page.find_element(*UserManagementPageLocators.ROLE)
        role.send_keys(get_user("User3")["role"])
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.ROLE_SELECTOR)
        self.assertEqual(get_user("User3")["role"], self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()

    def test_12_verify_that_User3_is_created_and_correctly_displayed(self):
        self.assertEqual(get_user("User3")["login"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LOGIN_3).text)
        self.assertEqual(get_user("User3")["name"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_FIRST_NAME_3).text)
        self.assertEqual(get_user("User3")["surname"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LAST_NAME_3).text)
        self.assertEqual("5 users",
                         self.user_page.find_element(*UserManagementPageLocators.FOOTER).text)

    def test_13_as_User1_create_User5(self):
        self.user_page.find_element(*BasePageLocators.USER_MANAGEMENT_TAB).click()
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.assertTrue(UserManagementPageLocators.ADD_NEW_USER_BUTTON_TEXT,
                        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).text)
        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_USER_BUTTON).click()
        name = self.user_page.find_element(*UserManagementPageLocators.FIRST_NAME)
        name.send_keys(get_user("User5")["name"])
        surname = self.user_page.find_element(*UserManagementPageLocators.LAST_NAME)
        surname.send_keys(get_user("User5")["surname"])
        login = self.user_page.find_element(*UserManagementPageLocators.LOGIN)
        login.send_keys(get_user("User5")["login"])
        password = self.user_page.find_element(*UserManagementPageLocators.PASSWORD)
        password.send_keys(get_user("User5")["password"])
        email = self.user_page.find_element(*UserManagementPageLocators.EMAIL)
        email.send_keys(get_user("User5")["email"])
        role = self.user_page.find_element(*UserManagementPageLocators.ROLE)
        role.send_keys(get_user("User5")["role"])
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.ROLE_SELECTOR)
        self.assertEqual(get_user("User5")["role"], self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()

    def test_14_verify_that_User5_is_created_and_correctly_displayed(self):
        self.assertEqual(get_user("User5")["login"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LOGIN_5).text)
        self.assertEqual(get_user("User5")["name"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_FIRST_NAME_5).text)
        self.assertEqual(get_user("User5")["surname"], self.user_page.find_element(
            *UserManagementPageLocators.LIST_LAST_NAME_5).text)
        self.assertEqual("6 users",
                         self.user_page.find_element(*UserManagementPageLocators.FOOTER).text)

    def test_15_as_User1_edit_User2_add_role_analyst(self):
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.user_page.find_element(*UserManagementPageLocators.USER2_CHECKBOX).click()
        self.user_page.find_element(*UserManagementPageLocators.EDIT_LINK).click()
        role = self.user_page.find_element(*UserManagementPageLocators.ROLE)
        role.send_keys(get_user("User2")["extended_role"])
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.ROLE_SELECTOR)
        self.assertEqual(get_user("User2")["extended_role"], self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()
        time.sleep(1)

    def test_16_as_User1_create_JXML_user_group(self):
        self.library_page.find_element(*BasePageLocators.USER_MANAGEMENT_TAB).click()
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.user_page.find_element(*UserManagementPageLocators.GROUPS_TAB).click()
        self.assertTrue(UserManagementPageLocators.ADD_NEW_GROUP_BUTTON_TEXT,
                        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_GROUP_BUTTON).text)
        self.user_page.find_element(*UserManagementPageLocators.ADD_NEW_GROUP_BUTTON).click()
        group_name = self.user_page.find_element(*UserManagementPageLocators.NEW_GROUP_NAME)
        group_name.send_keys(UserManagementPageLocators.JXML_GROUP_NAME_TEXT)
        group_description = self.user_page.find_element(*UserManagementPageLocators.NEW_GROUP_DESCRIPTION)
        group_description.send_keys(UserManagementPageLocators.JXML_GROUP_DESCRIPTION_TEXT)
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_NEW_GROUP_BUTTON)
        self.save.click()

    def test_17_verify_that_JXML_group_is_created_and_correctly_displayed_0_users(self):
        self.assertEqual(UserManagementPageLocators.JXML_GROUP_NAME_TEXT, self.user_page.find_element(
            *UserManagementPageLocators.JXML_GROUP_TABLE_NAME).text)
        self.assertEqual(UserManagementPageLocators.JXML_GROUP_DESCRIPTION_TEXT, self.user_page.find_element(
            *UserManagementPageLocators.JXML_GROUP_TABLE_DESCRIPTION).text)
        self.assertEqual("0", self.user_page.find_element(*UserManagementPageLocators.JXML_GROUP_USERS_COUNT).text)

    def test_18_as_User1_add_User2_User3_to_JXML_group(self):
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        # ADD USER2 TO JXML
        self.user_page.find_element(*UserManagementPageLocators.USERS_TAB).click()
        self.user_page.find_element(*UserManagementPageLocators.USER2_CHECKBOX).click()
        self.user_page.find_element(*UserManagementPageLocators.EDIT_LINK).click()
        role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER)
        role.send_keys(UserManagementPageLocators.JXML_GROUP_NAME_TEXT)
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER_SELECTOR)
        self.assertEqual(UserManagementPageLocators.JXML_GROUP_NAME_TEXT, self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()
        time.sleep(1)
        # ADD USER3 TO JXML
        self.user_page.find_element(*UserManagementPageLocators.USERS_TAB).click()
        self.user_page.find_element(*UserManagementPageLocators.USER3_CHECKBOX).click()
        self.user_page.find_element(*UserManagementPageLocators.EDIT_LINK).click()
        role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER)
        role.send_keys(UserManagementPageLocators.JXML_GROUP_NAME_TEXT)
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER_SELECTOR)
        self.assertEqual(UserManagementPageLocators.JXML_GROUP_NAME_TEXT, self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()
        time.sleep(1)

    def test_19_as_Admin_add_User1_to_JXML_DBA_groups_and_User4_to_JXML_group(self):
        self.library_page.find_element(*BasePageLocators.USER_MANAGEMENT_TAB).click()
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.user_page.find_element(*UserManagementPageLocators.GROUPS_TAB).click()
        # ADD USER1 TO DBA, JXML
        self.user_page.find_element(*UserManagementPageLocators.USERS_TAB).click()
        self.user_page.find_element(*UserManagementPageLocators.USER1_CHECKBOX).click()
        self.user_page.find_element(*UserManagementPageLocators.EDIT_LINK).click()
        role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER)
        role.send_keys(UserManagementPageLocators.JXML_GROUP_NAME_TEXT)
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER_SELECTOR)
        self.assertEqual(UserManagementPageLocators.JXML_GROUP_NAME_TEXT, self.select_role.text)
        self.select_role.click()
        role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER)
        role.send_keys(UserManagementPageLocators.DBA_GROUP_NAME_TEXT)
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER_SELECTOR)
        self.assertEqual(UserManagementPageLocators.DBA_GROUP_NAME_TEXT, self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()
        time.sleep(1)
        # ADD USER4 TO DBA
        self.user_page.find_element(*UserManagementPageLocators.USERS_TAB).click()
        self.user_page.find_element(*UserManagementPageLocators.USER4_CHECKBOX).click()
        self.user_page.find_element(*UserManagementPageLocators.EDIT_LINK).click()
        role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER)
        role.send_keys(UserManagementPageLocators.DBA_GROUP_NAME_TEXT)
        self.select_role = self.user_page.find_element(*UserManagementPageLocators.GROUPS_MEMBER_SELECTOR)
        self.assertEqual(UserManagementPageLocators.DBA_GROUP_NAME_TEXT, self.select_role.text)
        self.select_role.click()
        self.save = self.user_page.find_element(*UserManagementPageLocators.SAVE_BUTTON)
        self.save.click()
        time.sleep(1)

    def test_20_verify_that_all_needed_users_created_added_and_correctly_displayed_at_Groups_tab(self):
        self.assertTrue(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE)
        self.library_page.find_element(*UserManagementPageLocators.GROUPS_TAB).click()

        self.assertEqual(UserManagementPageLocators.JXML_GROUP_NAME_TEXT, self.user_page.find_element(
            *UserManagementPageLocators.JXML_GROUP_TABLE_NAME).text)
        self.assertEqual(UserManagementPageLocators.JXML_GROUP_DESCRIPTION_TEXT, self.user_page.find_element(
            *UserManagementPageLocators.JXML_GROUP_TABLE_DESCRIPTION).text)
        self.assertEqual("3", self.user_page.find_element(*UserManagementPageLocators.JXML_GROUP_USERS_COUNT).text)

        self.assertEqual(UserManagementPageLocators.DBA_GROUP_NAME_TEXT, self.user_page.find_element(
            *UserManagementPageLocators.DBA_GROUP_TABLE_NAME).text)
        self.assertEqual(UserManagementPageLocators.DBA_GROUP_DESCRIPTION_TEXT, self.user_page.find_element(
            *UserManagementPageLocators.DBA_GROUP_TABLE_DESCRIPTION).text)
        self.assertEqual("2", self.user_page.find_element(*UserManagementPageLocators.DBA_GROUP_USERS_COUNT).text)

        self.assertEqual("2 groups", self.user_page.find_element(*UserManagementPageLocators.GROUPS_TAB_FOOTER).text)

    @classmethod
    def tearDownClass(cls):
        # logout
        cls.user_page.logout()
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
