import unittest

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page import StatusBasePage


class ServiceTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # get the path of ChromeDriverServer
        # dir = os.path.dirname(__file__)
        # chrome_driver_path = dir + "\chromedriver.exe"

        # create a new Chrome session
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("start-maximized")
        executable_path = os.path.join(os.path.abspath(os.curdir), "frontend\program_data\chromedriver.exe")
        cls.driver = webdriver.Chrome(
            executable_path=executable_path,
            chrome_options=chrome_options)
        cls.driver.implicitly_wait(1)

        # create a new Firefox session
        # cls.driver = webdriver.Firefox()
        # cls.driver.implicitly_wait(15)
        # cls.driver.maximize_window()

        # navigate to the application login page
        cls.driver.get("http://localhost:9091/status")

        cls.status_page = StatusBasePage(cls.driver)
        cls.ml_build_info = cls.status_page.get_ml_build_info()

    def test_01_check_service_status(self):
        self.assertTrue(self.status_page.check_service_status())
        self.status_page.get_screen_shot("test_01_check_service_status.png")

    def test_02_get_ml_build_info(self):
        print(self.ml_build_info[1:])
        # return self.ml_build_info[1:] if self.test_01_check_service_status() else False

    def test_03_verify_that_ml_service_running(self):
        self.assertEqual("running", self.ml_build_info[0]["state"])

    def test_04_verify_event_storage_is_cassandra(self):
        self.assertEqual("cassandra", self.ml_build_info[0]["eventStorage.type"])

    def test_05_verify_hosts_connected_to_cassandra(self):
        self.assertEqual("connectedHosts: 1", self.ml_build_info[0]["eventStorage.state"].split(";")[0])

    def test_06_verify_cassandra_open_connections(self):
        self.assertEqual(" openConnections: 1", self.ml_build_info[0]["eventStorage.state"].split(";")[1])

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
