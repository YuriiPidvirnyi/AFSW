import json

import time

from pywinauto.application import Application
from pywinauto.keyboard import SendKeys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *
from element import BasePageElement, get_user, get_input_path_and_file


class StatusBasePage(BasePageElement):
    def check_service_status(self):
        return True if self.open(port=':9091', resource='/status') else False

    def get_ml_build_info(self):
        row = self.find_element(By.CSS_SELECTOR, "pre").text
        row_data = json.loads(row)
        ml_ver = "Machine Learning version: {}".format(row_data["version"])
        build_time = row_data["buildDate"].replace("T", " ").rstrip("Z")
        # self.build_time = self.build_time.rstrip("Z")
        return row_data, ml_ver, build_time


class LoginBasePage(BasePageElement):
    def check_page_loaded(self):
        return True if self.find_element(*LoginPageLocators.LOGIN_PAGE) else False

    def get_swarm_build_info(self):
        build_info = self.find_element(*LoginPageLocators.BUILD_INFO)
        return build_info if self.check_page_loaded() else False

    def enter_login(self, user):
        self.find_element(*LoginPageLocators.LOGIN).send_keys(get_user(user)["login"])

    def enter_password(self, user):
        self.find_element(*LoginPageLocators.PASSWORD).send_keys(get_user(user)["password"])

    def click_sign_in_button(self):
        self.find_element(*LoginPageLocators.SIGN_IN).click()

    def login(self, user):
        self.enter_login(user)
        self.enter_password(user)
        self.click_sign_in_button()

    def login_with_valid_user(self, user):
        self.login(user)
        return LibraryBasePage(self.driver)

    def login_with_invalid_user(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocators.ERROR_MESSAGE).text

    def login_with_invalid_login(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocators.ERROR_MESSAGE_LOGIN).text

    def login_with_invalid_password(self, user):
        self.login(user)
        return self.find_element(*LoginPageLocators.ERROR_MESSAGE_PASSWORD).text


class DashboardBasePage(BasePageElement):
    def check_page_loaded(self):
        try:
            self.find_element(*DashboardPageLocators.WELCOME)
        except NoSuchElementException:
            return False
        else:
            return True

    def logout(self):
        try:
            self.hover(*BasePageLocators.USER_CIRCLE_ICON)
            self.hover(*BasePageLocators.USER_AVATAR_MENU)
            self.hover(*BasePageLocators.USER_AVATAR_MENU_LOGOUT)
        except NoSuchElementException:
            time.sleep(5)
            self.find_element(*BasePageLocators.USER_AVATAR_MENU_LOGOUT).click()
        else:
            self.find_element(*BasePageLocators.USER_AVATAR_MENU_LOGOUT).click()


class LibraryBasePage(BasePageElement):
    def check_page_loaded(self):
        try:
            self.find_element(*LibraryPageLocators.LIBRARY_TAB_ACTIVE)
        except NoSuchElementException:
            time.sleep(5)
            return True if self.find_element(*LibraryPageLocators.LIBRARY_TAB_ACTIVE) else False
        else:
            return True if self.find_element(*LibraryPageLocators.LIBRARY_TAB_ACTIVE) else False

    def click_on_logo(self):
        self.find_element(*BasePageLocators.LOGO).click()

    def logout(self):
        try:
            self.hover(*BasePageLocators.USER_CIRCLE_ICON)
            self.hover(*BasePageLocators.USER_AVATAR_MENU)
            self.hover(*BasePageLocators.USER_AVATAR_MENU_LOGOUT)
        except NoSuchElementException:
            time.sleep(5)
            self.find_element(*BasePageLocators.USER_AVATAR_MENU_LOGOUT).click()
        else:
            self.find_element(*BasePageLocators.USER_AVATAR_MENU_LOGOUT).click()

    def folder_creation(self, amount=1):
        csv_files = get_input_path_and_file("csv")[1]
        csv_file = get_input_path_and_file("csv")[1][1]
        input_files_path = get_input_path_and_file("csv")[0]
        n = 0
        amount = range(amount + 1)[1:]
        for i in amount.__reversed__():
            time.sleep(1)
            self.find_element(*LibraryPageLocators.NEW_FOLDER).click()
            if self.is_element_present(*LibraryPageLocators.INPUT_FOLDER):
                input_folder = self.find_element(*LibraryPageLocators.INPUT_FOLDER)
                input_folder.send_keys(i, Keys.ENTER)
                time.sleep(1)
            else:
                SendKeys("{}".format(i))
                SendKeys('{ENTER 2}')
                time.sleep(1)
            n += 1
            time.sleep(3)
            if str(i) in self.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text and n == 1:
                self.find_element(*LibraryPageLocators.NEW_BUTTON).click()
                self.find_element(*LibraryPageLocators.NEW_WORKSPACE).click()
                elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
                elem.send_keys("Project_{}".format(i))
                time.sleep(1)
                SendKeys("{ENTER 2}")
                time.sleep(3)
                self.find_element(*LibraryPageLocators.SAVE_WORKSPACE_MENU).click()
                time.sleep(0.1)
                self.find_element(*LibraryPageLocators.SAVE_AND_EXIT_WORKSPACE).click()
                time.sleep(0.3)
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".main-table__cell-name-name"))).click()
                # self.find_element(*LibraryPageLocators.FIRST_FOLDER).click()
            elif str(i) in self.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text and n == 2:
                self.find_element(*LibraryPageLocators.NEW_BUTTON).click()
                self.find_element(*LibraryPageLocators.NEW_WORKSPACE).click()
                elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
                elem.send_keys("Project_{}".format(i))
                time.sleep(1)
                SendKeys("{ENTER 2}")
                time.sleep(3)
                self.find_element(*LibraryPageLocators.SAVE_WORKSPACE_MENU).click()
                time.sleep(0.1)
                self.find_element(*LibraryPageLocators.SAVE_AND_EXIT_WORKSPACE).click()
                time.sleep(0.3)
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".main-table__cell-name-name-wrapper"))).click()
                # self.find_element(*LibraryPageLocators.SECOND_FOLDER).click()
            elif str(i) in self.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text and n > 2:
                self.find_element(*LibraryPageLocators.NEW_BUTTON).click()
                self.find_element(*LibraryPageLocators.NEW_WORKSPACE).click()
                elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "input")))
                elem.send_keys("Project_{}".format(i))
                time.sleep(1)
                SendKeys("{ENTER 2}")
                time.sleep(3)
                self.find_element(*LibraryPageLocators.SAVE_WORKSPACE_MENU).click()
                time.sleep(0.1)
                self.find_element(*LibraryPageLocators.SAVE_AND_EXIT_WORKSPACE).click()
                time.sleep(0.3)
                WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".main-table__cell-name-inner-wrapper"))).click()
                # self.find_element(*LibraryPageLocators.THIRD_FOLDER).click()
            else:
                print("Some ERROR occurs!")
                return False
        else:
            self.find_element(*LibraryPageLocators.NEW_BUTTON).click()
            upload_file = self.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE)
            upload_file.click()
            time.sleep(1)
            app = Application().Connect(title=u'Open', class_name='#32770')
            window = app.Open
            window.Breadcrumb.Toolbar.click()
            # TODO: add input_data_sources path to configs
            window.TypeKeys(input_files_path)
            SendKeys('{ENTER 2}')
            window.ComboBox.click()
            # TODO: add input_data_sources filename to configs
            SendKeys(csv_file)
            SendKeys('{ENTER 2}')
            time.sleep(3)
            self.find_element(*LibraryPageLocators.ADD_DS_SAVE_BUTTON).click()
            time.sleep(3)
            self.find_element(*LibraryPageLocators.MY_LIBRARY).click()
            return True


class UserManagementBasePage(BasePageElement):
    def check_page_loaded(self):
        return True if self.find_element(*UserManagementPageLocators.USER_MANAGEMENT_TAB_ACTIVE) else False

    def click_on_logo(self):
        self.find_element(*BasePageLocators.LOGO).click()

    def logout(self):
        try:
            self.hover(*BasePageLocators.USER_CIRCLE_ICON)
            self.hover(*BasePageLocators.USER_AVATAR_MENU)
            self.hover(*BasePageLocators.USER_AVATAR_MENU_LOGOUT)
        except NoSuchElementException:
            time.sleep(5)
            self.find_element(*BasePageLocators.USER_AVATAR_MENU_LOGOUT).click()
        else:
            self.find_element(*BasePageLocators.USER_AVATAR_MENU_LOGOUT).click()
