import unittest

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page import *


class InitialStateSwarmLibraryTest(unittest.TestCase):

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

    def test_01_verify_that_library_tab_is_active(self):
        self.login_page.login("Administrator")
        self.assertTrue(self.library_page.check_page_loaded())

    def test_02_verify_that_page_header_exists(self):
        self.assertTrue(self.library_page.find_element(*BasePageLocators.PAGE_HEADER))

    def test_03_verify_that_page_alert_section_exists(self):
        self.assertTrue(self.library_page.find_element(*BasePageLocators.PAGE_ALERT_SECTION))

    def test_04_verify_that_library_left_side_section_exists(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.LIBRARY_LEFT_SIDE_SECTION))

    def test_05_verify_that_library_body_exists(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.LIBRARY_BODY))

    def test_06_verify_that_library_body_header_exists(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.LIBRARY_BODY_SECTION_HEADER))

    def test_07_verify_that_library_table_section_exists(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.LIBRARY_BODY_SECTION))

    def test_08_verify_that_library_footer_exists(self):
        self.assertTrue(self.library_page.find_element(*BasePageLocators.PAGE_FOOTER))

    def test_09_verify_that_library_All_tab_exists_and_is_active(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.ALL_TAB))
        self.assertEqual("All", self.library_page.find_element(*LibraryPageLocators.ALL_TAB_ACTIVE).text)
        print("\n\tcriterion: All")

    def test_10_verify_that_library_Workspaces_tab_exists_and_is_inactive(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.WORKSPACES_TAB))
        self.assertNotEqual("Workspaces",
                            self.library_page.find_element(*LibraryPageLocators.WORKSPACES_TAB_ACTIVE).text)
        self.assertEqual("Workspaces", self.library_page.find_element(*LibraryPageLocators.WORKSPACES_TAB).text)
        print("\n\tcriterion: Workspaces")

    def test_11_verify_that_library_Data_Sources_tab_exists_and_is_inactive(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.DATA_SOURCES_TAB))
        self.assertNotEqual("Data Sources",
                            self.library_page.find_element(*LibraryPageLocators.DATA_SOURCES_TAB_ACTIVE).text)
        self.assertEqual("Data Sources", self.library_page.find_element(*LibraryPageLocators.DATA_SOURCES_TAB).text)
        print("\n\tcriterion: Data Sources")

    def test_12_verify_my_library_bread_crumbs_path_at_All_tab(self):
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY).text)

    def test_13_verify_All_tab_active_and_unclickable(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.ALL_TAB_ACTIVE))
        try:
            self.library_page.find_element(*LibraryPageLocators.ALL_TAB)
        except NoSuchElementException:
            print("All Tab is unclickable.")

    def test_14_verify_my_library_table_name_and_column_set_at_All_tab(self):
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_TEXT,
                         self.login_page.find_element(*LibraryPageLocators.MY_LIBRARY).text)
        print("\n\tcriterion: {}".format(LibraryPageLocators.MY_LIBRARY_TEXT))
        self.assertEqual(LibraryPageLocators.COLUMN_SET,
                         tuple(self.login_page.find_element(*LibraryPageLocators.TABLE_HEADER).text.split("\n")))
        print("\n\tcriterion: {}".format(LibraryPageLocators.COLUMN_SET))

    def test_15_verify_my_library_placeholder_at_All_tab(self):
        try:
            self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_PLACEHOLDER)
        except NoSuchElementException:
            print("Placeholder \"{}\" is not found. Library table is not empty".format(
                LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT))
        else:
            self.assertEqual(LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT,
                             self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_PLACEHOLDER).text)
            print("\n\tcriterion: {}".format(LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT))

    def test_16_verify_that_0_displays_on_library_footer_at_All_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER))
        self.assertEqual("0 folders, 0 workspaces, 0 data sources",
                         self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER).text)
        print("\n\tcriterion: {}".format("0 folders, 0 workspaces, 0 data sources"))

    def test_17_verify_that_new_button_exists_clickable_with_appropriate_menu_items_at_All_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON))
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_MENU))
        self.assertEqual(LibraryPageLocators.ADD_WEB_LINK_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.ADD_WEB_LINK).text)
        self.assertEqual(LibraryPageLocators.NEW_WORKSPACE_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.NEW_WORKSPACE).text)
        self.assertEqual(LibraryPageLocators.UPLOAD_LOCAL_FILE_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE).text)

    def test_18_verify_if_click_on_new_button_again_menu_disappears_at_All_tab(self):
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_UNCLICKABLE).click()
        try:
            self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_MENU)
            return False
        except NoSuchElementException:
            return True

    def test_19_verify_that_New_Folder_exists_and_clickable_at_All_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER))
        self.new_folder = self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER)
        self.assertEqual("New Folder", self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER).text)
        self.new_folder.click()
        time.sleep(0.5)
        self.library_page.find_element(*LibraryPageLocators.LIBRARY_LEFT_SIDE_SECTION).click()
        print("\n\tcriterion: {}".format("New Folder"))

    def test_20_verify_Workspaces_tab_active_and_clickable(self):
        self.library_page.find_element(*LibraryPageLocators.WORKSPACES_TAB).click()
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.WORKSPACES_TAB_ACTIVE))

    def test_21_verify_my_library_bread_crumbs_path_at_Workspaces_tab(self):
        self.library_page.find_element(*LibraryPageLocators.WORKSPACES_TAB).click()
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY).text)

    def test_22_verify_my_library_table_name_and_column_set_at_Workspaces_tab(self):
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_TEXT,
                         self.login_page.find_element(*LibraryPageLocators.MY_LIBRARY).text)
        print("\n\tcriterion: {}".format(LibraryPageLocators.MY_LIBRARY_TEXT))
        self.assertEqual(LibraryPageLocators.COLUMN_SET,
                         tuple(self.login_page.find_element(*LibraryPageLocators.TABLE_HEADER).text.split("\n")))
        print("\n\tcriterion: {}".format(LibraryPageLocators.COLUMN_SET))

    def test_23_verify_my_library_placeholder_at_Workspaces_tab(self):
        try:
            self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_PLACEHOLDER)
        except NoSuchElementException:
            print("Placeholder \"{}\" is not found. Library table is not empty".format(
                LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT))
        else:
            self.assertEqual(LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT,
                             self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_PLACEHOLDER).text)
            print("\n\tcriterion: {}".format(LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT))

    def test_24_verify_that_0_displays_on_library_footer_at_Workspaces_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER))
        self.assertEqual("0 folders, 0 workspaces",
                         self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER).text)
        print("\n\tcriterion: {}".format("0 folders, 0 workspaces"))

    def test_25_verify_that_new_button_exists_clickable_with_appropriate_menu_items_at_Workspace_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON))
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_MENU))
        self.assertEqual(LibraryPageLocators.ADD_WEB_LINK_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.ADD_WEB_LINK).text)
        self.assertEqual(LibraryPageLocators.NEW_WORKSPACE_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.NEW_WORKSPACE).text)
        self.assertEqual(LibraryPageLocators.UPLOAD_LOCAL_FILE_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE).text)

    def test_26_verify_if_click_on_new_button_again_menu_disappears_at_Workspaces_tab(self):
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_UNCLICKABLE).click()
        try:
            self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_MENU)
            return False
        except NoSuchElementException:
            return True

    def test_27_verify_that_New_Folder_exists_and_clickable_at_Workspaces_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER))
        self.new_folder = self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER)
        self.assertEqual("New Folder", self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER).text)
        self.new_folder.click()
        time.sleep(0.5)
        self.library_page.find_element(*LibraryPageLocators.LIBRARY_LEFT_SIDE_SECTION).click()
        print("\n\tcriterion: {}".format("New Folder"))

    def test_28_verify_Data_Sources_tab_active_and_clickable(self):
        self.library_page.find_element(*LibraryPageLocators.DATA_SOURCES_TAB).click()
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.DATA_SOURCES_TAB_ACTIVE))

    def test_29_verify_my_library_bread_crumbs_path_at_Data_Sources_tab(self):
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.MY_LIBRARY).text)

    def test_30_verify_my_library_table_name_and_column_set_at_Data_Sources_tab(self):
        self.assertEqual(LibraryPageLocators.MY_LIBRARY_TEXT,
                         self.login_page.find_element(*LibraryPageLocators.MY_LIBRARY).text)
        print("\n\tcriterion: {}".format(LibraryPageLocators.MY_LIBRARY_TEXT))
        self.assertEqual(LibraryPageLocators.COLUMN_SET,
                         tuple(self.login_page.find_element(*LibraryPageLocators.TABLE_HEADER).text.split("\n")))
        print("\n\tcriterion: {}".format(LibraryPageLocators.COLUMN_SET))

    def test_31_verify_my_library_placeholder_at_Data_Sources_tab(self):
        try:
            self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_PLACEHOLDER)
        except NoSuchElementException:
            print("Placeholder \"{}\" is not found. Library table is not empty".format(
                LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT))
        else:
            self.assertEqual(LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT,
                             self.library_page.find_element(*LibraryPageLocators.MAIN_TABLE_PLACEHOLDER).text)
            print("\n\tcriterion: {}".format(LibraryPageLocators.MAIN_TABLE_PLACEHOLDER_TEXT))

    def test_32_verify_that_0_displays_on_library_footer_at_Data_Sources_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER))
        self.assertEqual("0 folders, 0 data sources",
                         self.library_page.find_element(*LibraryPageLocators.ALL_TABS_FOOTER).text)
        print("\n\tcriterion: {}".format("0 folders, 0 data sources"))

    def test_33_verify_that_new_button_exists_clickable_with_appropriate_menu_items_at_Data_Sources_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON))
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON).click()
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_MENU))
        self.assertEqual(LibraryPageLocators.ADD_WEB_LINK_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.ADD_WEB_LINK).text)
        self.assertEqual(LibraryPageLocators.NEW_WORKSPACE_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.NEW_WORKSPACE).text)
        self.assertEqual(LibraryPageLocators.UPLOAD_LOCAL_FILE_TEXT,
                         self.library_page.find_element(*LibraryPageLocators.UPLOAD_LOCAL_FILE).text)

    def test_34_verify_if_click_on_new_button_again_menu_disappears_at_Data_Sources_tab(self):
        self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_UNCLICKABLE).click()
        try:
            self.library_page.find_element(*LibraryPageLocators.NEW_BUTTON_MENU)
            return False
        except NoSuchElementException:
            return True

    def test_35_verify_that_New_Folder_exists_and_clickable_at_Data_Sources_tab(self):
        self.assertTrue(self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER))
        self.new_folder = self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER)
        self.assertEqual("New Folder", self.library_page.find_element(*LibraryPageLocators.NEW_FOLDER).text)
        self.new_folder.click()
        time.sleep(0.5)
        self.library_page.find_element(*LibraryPageLocators.LIBRARY_LEFT_SIDE_SECTION).click()
        print("\n\tcriterion: {}".format("New Folder"))

    #
    # def test_07_verify_that_admin_can_add_new_workspace(self):
    #     self.driver.find_element_by_css_selector("li.dropdown-base__list-item:nth-child(1)").click()
    #     elem = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "input_data_sources")))
    #     elem.send_keys(ADMIN_WORKSPACE)
    #     self.driver.find_element_by_css_selector(".dropdown-in-button__button").click()
    #     self.driver.find_element_by_css_selector("li.dropdown-base__list-item:nth-child(2)").click()
    #     self.assertEqual(ADMIN_WORKSPACE,
    #                      self.driver.find_element_by_css_selector(".main-table__cell-name-name").text)
    #
    # def test_08_verify_that_NewWorkspaceForAdmin_in_recent_updates_widget(self):
    #     if self.is_element_present(By.TAG_NAME, "use"):
    #         try:
    #             self.driver.find_element_by_tag_name("use").click()
    #         except WebDriverException:
    #             self.driver.find_element_by_css_selector(
    #                 '#page > div > div:nth-child(2) > div:nth-child(1) > header > div:nth-child(1) > a > svg').click()
    #     elem = self.driver.find_element_by_class_name("dashboard__widget-table_cell-name")
    #     self.assertTrue(elem)
    #     self.assertEqual(ADMIN_WORKSPACE, elem.text)
    #
    # def test_09_verify_that_admin_can_make_full_share_NewWorkspaceForAdmin_from_list(self):
    #     self.driver.find_element_by_css_selector("li.top-menu__item:nth-child(1) > a:nth-child(1)").click()
    #     self.driver.find_element_by_css_selector(".share-items__icon-text").click()
    #     self.driver.find_element_by_css_selector(".dropdown-with-caption__caption-block").click()
    #     self.driver.find_element_by_css_selector(
    #         "li.dropdown-base__list-item:nth-child(3) > span:nth-child(1) > p:nth-child(1)").click()
    #     self.driver.find_element_by_css_selector("button.button:nth-child(2)").click()
    #
    # def test_10_verify_that_hint_appears_when_user_hover_over_shared_icon(self):
    #     elem = self.driver.find_element_by_css_selector("svg.share-items__item")
    #     hover = ActionChains(self.driver).move_to_element(elem)
    #     hover.perform()
    #     self.assertEqual("Everyone", self.driver.find_element_by_css_selector(".popup-hint-title").text)
    #
    # def test_11_verify_that_NewWorkspaceForAdmin_in_shared_with_me_widget(self):
    #     if self.is_element_present(By.TAG_NAME, "use"):
    #         try:
    #             self.driver.find_element_by_tag_name("use").click()
    #         except WebDriverException:
    #             self.driver.find_element_by_css_selector(
    #                 '#page > div > div:nth-child(2) > div:nth-child(1) > header > div:nth-child(1) > a > svg').click()
    #     elem = self.driver.find_element_by_css_selector(
    #         "article.widget:nth-child(2) > section:nth-child(2) > ul:nth-child(1) > li:nth-child(1) > p:nth-child(2)")
    #     self.assertTrue(elem)
    #     self.assertEqual(ADMIN_WORKSPACE, elem.text)
    #
    # def test_12_verify_that_like_link_appears_when_user_hover_over_unfilled_heart_icon(self):
    #     self.driver.find_element_by_css_selector("li.top-menu__item:nth-child(1) > a:nth-child(1)").click()
    #     elem = self.driver.find_element_by_css_selector(".fa")
    #     self.assertTrue(elem)
    #     hover = ActionChains(self.driver).move_to_element(elem)
    #     hover.perform()
    #     self.assertEqual("Like",
    #                      self.driver.find_element_by_css_selector(".main-table__cell-liked-icon_like-link").text)
    #
    # def test_13_verify_that_admin_can_like_workspace(self):
    #     self.driver.find_element_by_css_selector("li.top-menu__item:nth-child(1) > a:nth-child(1)").click()
    #     elem = self.driver.find_element_by_css_selector(".fa")
    #     self.assertTrue(elem)
    #     hover = ActionChains(self.driver).move_to_element(elem)
    #     hover.perform()
    #     self.like_link = self.driver.find_element_by_css_selector(".main-table__cell-liked-icon_like-link")
    #     self.assertTrue(self.like_link)
    #     self.assertEqual("Like", self.like_link.text)
    #     self.like_link.click()
    #
    # def test_14_verify_that_heart_icon_filled_with_1_counter(self):
    #     self.assertTrue(self.driver.find_element_by_css_selector(".fa"))
    #     self.assertTrue(self.driver.find_element_by_class_name("fa-heart"))
    #     self.like_counter = self.driver.find_element_by_class_name("main-table__cell-liked-icon_likes-count")
    #     self.like_div = self.driver.find_element_by_css_selector(".main-table__cell-liked-icon")
    #     self.assertEqual("1", self.like_div.get_attribute('textContent')[0])
    #
    #     # print("innerHTML", self.like_div.get_attribute("innerHTML"))
    #     # print(self.driver.execute_script("return arguments[0].innerHTML", self.like_div))
    #
    #     # print('textContent', self.like_div.get_attribute('textContent')[0])
    #     # print(self.driver.execute_script("return arguments[0].textContent", self.like_div))
    #
    # def test_15_verify_that_dislike_link_appears_when_user_hover_over_filled_heart_icon(self):
    #     self.driver.find_element_by_css_selector("li.top-menu__item:nth-child(1) > a:nth-child(1)").click()
    #     elem = self.driver.find_element_by_css_selector(".fa")
    #     self.assertTrue(elem)
    #     hover = ActionChains(self.driver).move_to_element(elem)
    #     hover.perform()
    #     self.assertEqual("Dislike",
    #                      self.driver.find_element_by_css_selector(".main-table__cell-liked-icon_like-link").text)
    #
    # def test_16_verify_that_admin_can_dislike_workspace(self):
    #     self.driver.find_element_by_css_selector("li.top-menu__item:nth-child(1) > a:nth-child(1)").click()
    #     elem = self.driver.find_element_by_css_selector(".fa")
    #     self.assertTrue(elem)
    #     hover = ActionChains(self.driver).move_to_element(elem)
    #     hover.perform()
    #     self.like_link = self.driver.find_element_by_css_selector(".main-table__cell-liked-icon_like-link")
    #     self.assertTrue(self.like_link)
    #     self.assertEqual("Dislike", self.like_link.text)
    #     self.like_link.click()
    #
    # def test_17_verify_that_heart_icon_unfiled_with_0_counter(self):
    #     self.assertTrue(self.driver.find_element_by_css_selector(".fa"))
    #     self.assertTrue(self.driver.find_element_by_class_name("fa-heart"))
    #     self.like_counter = self.driver.find_element_by_class_name("main-table__cell-liked-icon_likes-count")
    #     self.like_div = self.driver.find_element_by_css_selector(".main-table__cell-liked-icon")
    #     self.assertEqual("0", self.like_div.get_attribute('textContent')[0])
    #
    #     # print("innerHTML", self.like_div.get_attribute("innerHTML"))
    #     # print(self.driver.execute_script("return arguments[0].innerHTML", self.like_div))
    #
    #     # print('textContent', self.like_div.get_attribute('textContent')[0])
    #     # print(self.driver.execute_script("return arguments[0].textContent", self.like_div))

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
