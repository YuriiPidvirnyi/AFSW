import json
import unittest
import webbrowser

import shutil

import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import HTMLTestRunner

from ServiceStatusTestCases import ServiceTest
from LoginTestCases import InitialStateLogInTest
from DashboardTestCasesNotifications import NotificationTest
from DashboardTestCasesMain import InitialStateDashboardTest
from LibraryTestCases import InitialStateSwarmLibraryTest
from EnvironmentPreparationUser import CreateUsersGroupsAndAddUsersToGroups
from EnvironmentPreparationData import CreateFoldersConnectionProjectsAndDataSources

# get the directory path to output report file
reports_dir = os.path.join(os.getcwd(), "frontend\output_reports")
screen_shots_dir = os.path.join(reports_dir, "screenshots")

if os.path.exists(reports_dir):
    shutil.rmtree(reports_dir)
os.mkdir(reports_dir)
if not os.path.exists(screen_shots_dir):
    os.mkdir(screen_shots_dir)

reports_dir = os.path.join(os.getcwd(), "frontend\output_reports")

# open the report file
outfile = open(reports_dir + "\SmokeTestRunSummary.html", "w")

# get all tests from SearchText and HomePageTest class
service = unittest.TestLoader().loadTestsFromTestCase(ServiceTest)
initial_login = unittest.TestLoader().loadTestsFromTestCase(InitialStateLogInTest)
initial_dashboard = unittest.TestLoader().loadTestsFromTestCase(InitialStateDashboardTest)
initial_dashboard_notifications = unittest.TestLoader().loadTestsFromTestCase(NotificationTest)
initial_library = unittest.TestLoader().loadTestsFromTestCase(InitialStateSwarmLibraryTest)
env_prep_user = unittest.TestLoader().loadTestsFromTestCase(CreateUsersGroupsAndAddUsersToGroups)
env_prep_data = unittest.TestLoader().loadTestsFromTestCase(CreateFoldersConnectionProjectsAndDataSources)

# create a test suite combining search_text and home_page_test
# test_suite = unittest.TestSuite([service, login, dashboard, library, user_management])
test_suite = unittest.TestSuite(
    [service, initial_login, initial_dashboard, initial_dashboard_notifications, initial_library, env_prep_user,
     env_prep_data, ])


def test_report_enhancement(file_path=None):
    # get the path of ChromeDriverServer
    # dir = os.path.dirname(__file__)
    # chrome_driver_path = dir + "\chromedriver.exe"

    # create a new Chrome session
    options = Options()
    options.add_argument("--headless")
    executable_path = os.path.join(os.path.abspath(os.curdir), "frontend\program_data\chromedriver.exe")
    driver = webdriver.Chrome(
        executable_path=executable_path,
        chrome_options=options)
    driver.implicitly_wait(1)
    # driver.maximize_window()

    # create a new Firefox session
    # driver = webdriver.Firefox()
    # driver.implicitly_wait(15)
    # driver.maximize_window()

    # navigate to the application login page
    driver.get("http://localhost:8080/#/login")
    swarm_info = driver.find_element_by_css_selector(".login-side-right__footer").text
    swarm = swarm_info.split("|")[0]
    # driver.quit()
    driver.get("http://localhost:9091/status")
    row = driver.find_element_by_tag_name("pre").text
    row_data = json.loads(row)
    ml_ver = "Machine Learning version: {}".format(row_data["version"])
    build_time = row_data["buildDate"].replace("T", " ")
    build_time = build_time.rstrip("Z")
    # time.sleep(60)
    driver.quit()
    return swarm, ml_ver, build_time


# print(test_report_enhancement())
enhancements = test_report_enhancement()
swarm = enhancements[0]
ml = enhancements[1]
build_time = enhancements[2]

# configure HTMLTestRunner options
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='Test Report',
                                       description='Smoke Tests on build: {} | {} | Build Date: {}'.format(swarm, ml,
                                                                                                           build_time))

# run the suite using HTMLTestRunner
# unittest.TextTestRunner(verbosity=2).run(test_suite)
runner.run(test_suite)

report_file = os.path.join(reports_dir + "\SmokeTestRunSummary.html")

webbrowser.open(report_file)

# open_test_report()
