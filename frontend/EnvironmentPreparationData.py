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


class CreateFoldersConnectionProjectsAndDataSources(unittest.TestCase):

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

    def test_01_as_admin_create_CSV_folder(self):
        self.login_page.login("Administrator")
        self.library_page.check_page_loaded()
        time.sleep(1)
        self.new_folder = self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER)
        self.assertTrue(self.new_folder)
        self.new_folder.click()
        time.sleep(5)
        # self.elem = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.TAG_NAME, "input_data_sources")))
        # SendKeys("{}".format(LibraryPageLocators.MY_LIBRARY_CSV_FOLDER_NAME))
        # SendKeys('{ENTER 2}')
        if self.library_page.is_element_present(*LibraryPageLocators.INPUT_FOLDER):
            input_folder = self.library_page.find_element(*LibraryPageLocators.INPUT_FOLDER)
            input_folder.send_keys(LibraryPageLocators.MY_LIBRARY_CSV_FOLDER_NAME, Keys.ENTER)
        else:
            SendKeys("{}".format(LibraryPageLocators.MY_LIBRARY_CSV_FOLDER_NAME))
            SendKeys('{ENTER 2}')
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.MY_LIBRARY_CSV_FOLDER):
            self.assertEqual(LibraryPageLocators.MY_LIBRARY_CSV_FOLDER_NAME,
                             self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY_CSV_FOLDER).text)
        else:
            time.sleep(3)
            self.assertEqual(LibraryPageLocators.MY_LIBRARY_CSV_FOLDER_NAME,
                             self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY_CSV_FOLDER).text)

    def test_02_as_Admin_add_CSV_file_to_appropriate_folder(self):
        self.assertTrue(*LibraryPageLocators.LIBRARY_TAB_ACTIVE)

        # ADD CSV FILE
        self.csv_files = get_input_path_and_file("csv")[1]
        self.csv_file = get_input_path_and_file("csv")[1][0]
        self.input_files_path = get_input_path_and_file("csv")[0]
        csv_folder = self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY_CSV_FOLDER)
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_CSV_FOLDER_NAME, csv_folder.text)
        csv_folder.click()
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        upload_file = self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE)
        upload_file.click()
        time.sleep(1)
        app = Application().Connect(title=u'Open', class_name='#32770')
        window = app.Open
        window.Breadcrumb.Toolbar.click()
        # TODO: add input_data_sources path to configs
        window.TypeKeys(self.input_files_path)
        SendKeys('{ENTER 2}')
        window.ComboBox.click()
        # TODO: add input_data_sources filename to configs
        SendKeys(self.csv_file)
        SendKeys('{ENTER 2}')
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_SAVE_BUTTON).click()
        time.sleep(3)
        self.library_page.logout()

    def test_03_as_User1_create_JSON_XML_HTML_EXCEL_ACCESS_folders(self):
        self.login_page.login("User1")
        self.library_page.check_page_loaded()
        time.sleep(5)

        # ADD JSON
        new_folder = self.user_page.find_element(*LibraryPageLocators.NEW_FOLDER)
        new_folder.click()
        time.sleep(5)
        if self.library_page.is_element_present(*LibraryPageLocators.INPUT_FOLDER):
            input_folder = self.library_page.find_element(*LibraryPageLocators.INPUT_FOLDER)
            input_folder.send_keys(LibraryPageLocators.MY_LIBRARY_JSON_FOLDER_NAME, Keys.ENTER)
        else:
            SendKeys("{}".format(LibraryPageLocators.MY_LIBRARY_JSON_FOLDER_NAME))
            SendKeys('{ENTER 2}')
        if self.library_page.is_element_present(*LibraryPageLocators.MAIN_TABLE_BODY):
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_JSON_FOLDER_NAME, self.library_items)
        else:
            time.sleep(3)
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_JSON_FOLDER_NAME, self.library_items)

        # ADD XML
        new_folder.click()
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.INPUT_FOLDER):
            input_folder = self.library_page.find_element(*LibraryPageLocators.INPUT_FOLDER)
            input_folder.send_keys(LibraryPageLocators.MY_LIBRARY_XML_FOLDER_NAME, Keys.ENTER)
        else:
            SendKeys("{}".format(LibraryPageLocators.MY_LIBRARY_XML_FOLDER_NAME))
            SendKeys('{ENTER 2}')
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.MAIN_TABLE_BODY):
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_XML_FOLDER_NAME, self.library_items)
        else:
            time.sleep(3)
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_XML_FOLDER_NAME, self.library_items)

        # ADD HTML
        new_folder.click()
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.INPUT_FOLDER):
            input_folder = self.library_page.find_element(*LibraryPageLocators.INPUT_FOLDER)
            input_folder.send_keys(LibraryPageLocators.MY_LIBRARY_HTML_FOLDER_NAME, Keys.ENTER)
        else:
            SendKeys("{}".format(LibraryPageLocators.MY_LIBRARY_HTML_FOLDER_NAME))
            SendKeys('{ENTER 2}')
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.MAIN_TABLE_BODY):
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_HTML_FOLDER_NAME, self.library_items)
        else:
            time.sleep(3)
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_HTML_FOLDER_NAME, self.library_items)

        # ADD EXCEL
        new_folder.click()
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.INPUT_FOLDER):
            input_folder = self.library_page.find_element(*LibraryPageLocators.INPUT_FOLDER)
            input_folder.send_keys(LibraryPageLocators.MY_LIBRARY_EXCEL_FOLDER_NAME, Keys.ENTER)
        else:
            SendKeys("{}".format(LibraryPageLocators.MY_LIBRARY_EXCEL_FOLDER_NAME))
            SendKeys('{ENTER 2}')
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.MAIN_TABLE_BODY):
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_EXCEL_FOLDER_NAME, self.library_items)
        else:
            time.sleep(3)
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_EXCEL_FOLDER_NAME, self.library_items)

        # ADD ACCESS
        new_folder.click()
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.INPUT_FOLDER):
            input_folder = self.library_page.find_element(*LibraryPageLocators.INPUT_FOLDER)
            input_folder.send_keys(LibraryPageLocators.MY_LIBRARY_ACCESS_FOLDER_NAME, Keys.ENTER)
        else:
            SendKeys("{}".format(LibraryPageLocators.MY_LIBRARY_ACCESS_FOLDER_NAME))
            SendKeys('{ENTER 2}')
        time.sleep(1)
        if self.library_page.is_element_present(*LibraryPageLocators.MAIN_TABLE_BODY):
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_ACCESS_FOLDER_NAME, self.library_items)
        else:
            time.sleep(3)
            self.library_items = self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_BODY).text
            self.assertIn(LibraryPageLocators.MY_LIBRARY_ACCESS_FOLDER_NAME, self.library_items)

        self.driver.refresh()
        time.sleep(1)

    def test_04_as_User1_add_datasources_to_appropriate_folders(self):
        self.assertTrue(*LibraryPageLocators.LIBRARY_TAB_ACTIVE)
        time.sleep(1)

        # ADD ACCESS FILE
        self.access_files = get_input_path_and_file("mdb")[1]
        self.access_file = get_input_path_and_file("mdb")[1][0]
        self.input_files_path = get_input_path_and_file("mdb")[0]
        try:
            self.library_page.find_element(*LibraryPageLocators.ACCESS_FOLDER)
        except NoSuchElementException as e:
            # print(e)
            pass
        finally:
            time.sleep(5)
            access_folder = self.library_page.find_element(*LibraryPageLocators.ACCESS_FOLDER)
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_ACCESS_FOLDER_NAME, access_folder.text)
        access_folder.click()
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        upload_file = self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE)
        upload_file.click()
        time.sleep(1)
        app = Application().Connect(title=u'Open', class_name='#32770')
        window = app.Open
        window.Breadcrumb.Toolbar.click()
        # TODO: add input_data_sources path to configs
        window.TypeKeys(self.input_files_path)
        SendKeys('{ENTER 2}')
        window.ComboBox.click()
        # TODO: add input_data_sources filename to configs
        SendKeys(self.access_file)
        SendKeys('{ENTER 2}')
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_SAVE_BUTTON).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY).click()

        # ADD EXCEL FILE
        self.excel_files = get_input_path_and_file("xlsx")[1]
        self.excel_file = get_input_path_and_file("xlsx")[1][0]
        self.input_files_path = get_input_path_and_file("xlsx")[0]
        try:
            self.library_page.find_element(*LibraryPageLocators.EXCEL_FOLDER)
        except NoSuchElementException as e:
            # print(e)
            pass
        finally:
            time.sleep(5)
            excel_folder = self.library_page.find_element(*LibraryPageLocators.EXCEL_FOLDER)
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_EXCEL_FOLDER_NAME, excel_folder.text)
        excel_folder.click()
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        upload_file = self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE)
        upload_file.click()
        time.sleep(1)
        window.Breadcrumb.Toolbar.click()
        # TODO: add input_data_sources path to configs
        window.TypeKeys(self.input_files_path)
        SendKeys('{ENTER 2}')
        window.ComboBox.click()
        # TODO: add input_data_sources filename to configs
        SendKeys(self.excel_file)
        SendKeys('{ENTER 2}')
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_SAVE_BUTTON).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY).click()

        # ADD HTML FILE
        self.html_files = get_input_path_and_file("html")[1]
        self.html_file = get_input_path_and_file("html")[1][0]
        self.input_files_path = get_input_path_and_file("html")[0]
        try:
            self.library_page.find_element(*LibraryPageLocators.HTML_FOLDER)
        except NoSuchElementException as e:
            # print(e)
            pass
        finally:
            time.sleep(5)
            html_folder = self.library_page.find_element(*LibraryPageLocators.HTML_FOLDER)
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_HTML_FOLDER_NAME, html_folder.text)
        html_folder.click()
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        upload_file = self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE)
        upload_file.click()
        time.sleep(1)
        window.Breadcrumb.Toolbar.click()
        # TODO: add input_data_sources path to configs
        window.TypeKeys(self.input_files_path)
        SendKeys('{ENTER 2}')
        window.ComboBox.click()
        # TODO: add input_data_sources filename to configs
        SendKeys(self.html_file)
        SendKeys('{ENTER 2}')
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_SAVE_BUTTON).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY).click()

        # ADD JSON FILE
        self.json_files = get_input_path_and_file("json")[1]
        self.json_file = get_input_path_and_file("json")[1][0]
        self.input_files_path = get_input_path_and_file("json")[0]
        try:
            self.library_page.find_element(*LibraryPageLocators.JSON_FOLDER)
        except NoSuchElementException as e:
            # print(e)
            pass
        finally:
            time.sleep(5)
            json_folder = self.library_page.find_element(*LibraryPageLocators.JSON_FOLDER)
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_JSON_FOLDER_NAME, json_folder.text)
        json_folder.click()
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        upload_file = self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE)
        upload_file.click()
        time.sleep(1)
        window.Breadcrumb.Toolbar.click()
        # TODO: add input_data_sources path to configs
        window.TypeKeys(self.input_files_path)
        SendKeys('{ENTER 2}')
        window.ComboBox.click()
        # TODO: add input_data_sources filename to configs
        SendKeys(self.json_file)
        SendKeys('{ENTER 2}')
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_SAVE_BUTTON).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY).click()

        # ADD XML FILE
        self.xml_files = get_input_path_and_file("xml")[1]
        self.xml_file = get_input_path_and_file("xml")[1][0]
        self.input_files_path = get_input_path_and_file("xml")[0]
        try:
            self.library_page.find_element(*LibraryPageLocators.XML_FOLDER)
        except NoSuchElementException as e:
            # print(e)
            pass
        finally:
            time.sleep(5)
            xml_folder = self.library_page.find_element(*LibraryPageLocators.XML_FOLDER)
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_XML_FOLDER_NAME, xml_folder.text)
        xml_folder.click()
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        upload_file = self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE)
        upload_file.click()
        time.sleep(1)
        window.Breadcrumb.Toolbar.click()
        # TODO: add input_data_sources path to configs
        window.TypeKeys(self.input_files_path)
        SendKeys('{ENTER 2}')
        window.ComboBox.click()
        # TODO: add input_data_sources filename to configs
        SendKeys(self.xml_file)
        SendKeys('{ENTER 2}')
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_SAVE_BUTTON).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY).click()

    def test_05_as_Admin_create_Local_File_System_Connection(self):
        self.library_page.logout()
        self.login_page.login("Administrator")
        self.library_page.check_page_loaded()
        time.sleep(1)
        self.user_page.find_element(*BasePageLocators.CONNECTIONS_TAB).click()
        self.assertEqual(BasePageLocators.CONNECTIONS_TAB_NAME,
                         self.user_page.find_element(*BasePageLocators.CONNECTIONS_TAB).text)
        self.assertTrue(self.library_page.find_element(*ConnectionsPageLocators.ADD_NEW_CONNECTION_BUTTON))
        self.add_connection = self.library_page.find_element(*ConnectionsPageLocators.ADD_NEW_CONNECTION_BUTTON)
        self.assertEqual(ConnectionsPageLocators.ADD_NEW_CONNECTION_BUTTON_NAME, self.add_connection.text)
        self.add_connection.click()
        self.library_page.find_element(*ConnectionsPageLocators.CONNECTION_NAME_INPUT).send_keys("InternalIrisDataSet")
        self.library_page.find_element(*ConnectionsPageLocators.DESCRIPTION_INPUT).send_keys("Iris Plants Database")
        self.library_page.find_element(*ConnectionsPageLocators.PATH_INPUT).send_keys(
            "c:\\Users\\Iurii_Pidvirnyi\\Projects\\Current Projects\\DWCH-ESM\\testing\\Test Data\\for_AFSW\\")
        self.library_page.find_element(*ConnectionsPageLocators.SAVE_NEW_CONNECTION_BUTTON).click()

    def test_06_verify_that_new_connection_created_and_correctly_displayed_at_grid(self):
        self.assertEqual("InternalIrisDataSet",
                         self.library_page.find_element(*ConnectionsPageLocators.IRIS_CONNECTION_NAME).text)
        self.assertEqual("Iris Plants Database",
                         self.library_page.find_element(*ConnectionsPageLocators.IRIS_CONNECTION_DESCRIPTION).text)
        self.assertTrue(self.library_page.find_element(*ConnectionsPageLocators.IRIS_CONNECTION_SHARE_LINK))
        time.sleep(1)

    def test_07_verify_that_new_item_added_to_New_button_menu(self):
        self.library_page.find_element(*BasePageLocators.LIBRARY_TAB).click()
        self.library_page.check_page_loaded()
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON))
        self.library_page.find_element(*BasePageLocators.LIBRARY_TAB).click()
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_MENU))
        self.assertEqual(LibraryPageLocators.ADD_WEB_LINK_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.ADD_WEB_LINK_AFTER_CONN).text)
        self.assertEqual(LibraryPageLocators.NEW_WORKSPACE_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.NEW_WORKSPACE).text)
        self.assertEqual(LibraryPageLocators.UPLOAD_LOCAL_FILE_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE).text)
        self.assertEqual(LibraryPageLocators.ADD_FROM_CONNECTION_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.ADD_FROM_CONNECTION).text)

    def test_08_as_Admin_add_file_from_connection_with_manually_defining_format(self):
        self.library_page.find_element(*LibraryPageLocators.ADD_FROM_CONNECTION).click()
        self.assertTrue(self.library_page.find_element(*ConnectionsPageLocators.IRIS_ADD_FROM_LINK))
        self.library_page.find_element(*ConnectionsPageLocators.IRIS_ADD_FROM_LINK).click()
        self.assertEqual("iris",
                         self.library_page.find_element(*ConnectionsPageLocators.IRIS_FILE_FROM_CONNECTION).text)
        self.library_page.find_element(*ConnectionsPageLocators.IRIS_FILE_FROM_CONNECTION).click()
        self.assertEqual("IRIS",
                         self.library_page.find_element(*ConnectionsPageLocators.SELECTED).text)
        self.library_page.find_element(*ConnectionsPageLocators.OPEN_BUTTON).click()
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_FORMAT_FIELD).click()
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_DELIMITED_FORMAT).click()
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_SAVE_BUTTON).click()
        time.sleep(1)

    def test_09_as_Admin_create_new_workspace_for_DBA_group(self):
        self.assertTrue(*LibraryPageLocators.LIBRARY_TAB_ACTIVE)
        time.sleep(1)
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        self.library_page.find_element(*LibraryPageLocators.NEW_WORKSPACE).click()
        self.elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "input")))
        self.elem.send_keys(LibraryPageLocators.DBA_WORKSPACE)
        time.sleep(1)
        SendKeys('{ENTER 2}')
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.SAVE_WORKSPACE_MENU).click()
        time.sleep(0.1)
        self.library_page.find_element(*LibraryPageLocators.SAVE_AND_EXIT_WORKSPACE).click()
        time.sleep(0.3)
        self.driver.refresh()
        time.sleep(0.1)

    def test_10_verify_that_new_workspace_created_and_correctly_displayed_in_grid(self):
        self.assertEqual(LibraryPageLocators.DBA_WORKSPACE,
                         self.library_page.find_element(*LibraryPageLocators.DBA_WORKSPACE_GRID_NAME).text)
        self.assertEqual("Workspace",
                         self.library_page.find_element(*LibraryPageLocators.DBA_WORKSPACE_GRID_TYPE).text)

    def test_11_as_Admin_add_DS_to_new_workspace_for_DBA_group(self):
        self.driver.refresh()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.DBA_WORKSPACE_GRID_CHECK_BOX).click()
        self.library_page.find_element(*LibraryPageLocators.EDIT_GRID_ITEM).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_TO_WRKS_ICON).click()
        self.library_page.find_element(*LibraryPageLocators.ADD_1_DS_TO_WRKS).click()
        self.library_page.find_element(*LibraryPageLocators.ADD_2_DS_TO_WRKS).click()
        self.library_page.find_element(*LibraryPageLocators.ADD_3_DS_TO_WRKS).click()
        time.sleep(0.5)
        self.library_page.find_element(*LibraryPageLocators.OPEN_SELECTED_BUTTON).click()
        time.sleep(5)
        self.library_page.find_element(*LibraryPageLocators.SAVE_WORKSPACE_MENU_ADD_WRKS).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.SAVE_AND_EXIT_WORKSPACE).click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

    def test_12_as_User1_create_new_workspace_for_JXML_group(self):
        self.library_page.logout()
        time.sleep(3)
        self.login_page.login("User1")
        self.library_page.check_page_loaded()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        self.library_page.find_element(*LibraryPageLocators.NEW_WORKSPACE).click()
        self.elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "input")))
        self.elem.send_keys(LibraryPageLocators.JXML_WORKSPACE)
        time.sleep(1)
        SendKeys('{ENTER 2}')
        time.sleep(10)
        self.library_page.find_element(*LibraryPageLocators.SAVE_WORKSPACE_MENU).click()
        time.sleep(0.1)
        self.library_page.find_element(*LibraryPageLocators.SAVE_AND_EXIT_WORKSPACE).click()
        time.sleep(0.3)
        self.driver.refresh()
        time.sleep(0.5)

    def test_13_verify_that_new_workspace_created_and_correctly_displayed_in_grid(self):
        try:
            self.library_page.find_element(*LibraryPageLocators.JXML_WORKSPACE_GRID_NAME)
        except NoSuchElementException:
            time.sleep(5)
        finally:
            self.assertEqual(LibraryPageLocators.JXML_WORKSPACE,
                             self.library_page.find_element(*LibraryPageLocators.JXML_WORKSPACE_GRID_NAME).text)
            self.assertEqual("Workspace",
                             self.library_page.find_element(*LibraryPageLocators.JXML_WORKSPACE_GRID_TYPE).text)

    def test_14_as_User1_add_DS_to_new_workspace_for_JXML_group(self):
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.JXML_WORKSPACE_GRID_CHECK_BOX).click()
        self.library_page.find_element(*LibraryPageLocators.EDIT_GRID_ITEM).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.ADD_DS_TO_WRKS_ICON).click()
        self.library_page.find_element(*LibraryPageLocators.ADD_1_DS_TO_WRKS).click()
        self.library_page.find_element(*LibraryPageLocators.ADD_2_DS_TO_WRKS).click()
        time.sleep(0.5)
        self.library_page.find_element(*LibraryPageLocators.OPEN_SELECTED_BUTTON).click()
        time.sleep(5)
        self.library_page.find_element(*LibraryPageLocators.SAVE_WORKSPACE_MENU_ADD_WRKS).click()
        time.sleep(3)
        self.library_page.find_element(*LibraryPageLocators.SAVE_AND_EXIT_WORKSPACE).click()
        time.sleep(3)
        self.driver.refresh()
        time.sleep(3)

    def test_15_as_User4_recursively_create_5_folders_with_objects_next_inside_previous(self):
        self.library_page.logout()
        self.login_page.login("User4")
        self.library_page.check_page_loaded()
        time.sleep(5)
        self.library_page.folder_creation(5)

    def test_16_verify_that_environment_prepared_as_expected(self):
        self.library_page.logout()
        for i in range(6):
            if i == 0:
                self.login_page.login("Administrator")
                self.library_page.check_page_loaded()
                time.sleep(10)
                self.assertEqual("7 folders, 3 workspaces, 1 data source",
                                 self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER).text)
                print("\n\tcriterion: {} for {}".format("7 folders, 3 workspaces, 1 data source", "Administrator"))
                self.library_page.logout()
            elif i != 0:
                self.login_page.login("User{}".format(str(i)))
                self.library_page.check_page_loaded()
                time.sleep(10)
                if i == 1:
                    self.assertEqual("5 folders, 1 workspace, 0 data sources",
                                     self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER).text)
                    print("\n\tcriterion: {} for User{}".format("5 folders, 1 workspace, 0 data sources", str(i)))
                elif i == 4:
                    self.assertEqual("1 folder, 1 workspace, 0 data sources",
                                     self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER).text)
                    print("\n\tcriterion: {} for User{}".format("1 folder, 1 workspace, 0 data sources", str(i)))
                else:
                    self.assertEqual("0 folders, 0 workspaces, 0 data sources",
                                     self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER).text)
                    print("\n\tcriterion: {} for User{}".format("0 folders, 0 workspaces, 0 data sources", str(i)))
                self.library_page.logout()
        else:
            self.login_page.login("Administrator")
            self.library_page.check_page_loaded()

    @classmethod
    def tearDownClass(cls):
        # logout
        cls.user_page.logout()
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
