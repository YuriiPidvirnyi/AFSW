import csv

import os
import shutil

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains

from PIL import Image


class BasePageElement(object):
    def __init__(self, driver, url='http://localhost', port='8080'):
        self.base_url = url + port
        self.main_url = url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, port=None, resource=None):
        url = self.main_url + port + resource
        try:
            self.driver.get(url)
            return True
        except:
            return False

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def is_element_present(self, *locator):
        try:
            self.find_element(*locator)
        except NoSuchElementException:
            return False
        return True

    def get_screen_shot(self, filename):
        reports_dir = os.path.join(os.getcwd(), "frontend\output_reports")
        screen_shots_dir = os.path.join(reports_dir, "screenshots")

        if not os.path.exists(reports_dir):
            os.mkdir(reports_dir)
            if not os.path.exists(screen_shots_dir):
                os.mkdir(screen_shots_dir)

        screen_shots_path = os.path.join(screen_shots_dir, filename)
        self.driver.get_screenshot_as_file(filename=screen_shots_path)
        print("\n\tPlease see output screenshot: \"{}\".".format(filename))

    def get_screen_shot_of_element(self, filename, element):
        screen_shot_path = os.path.join(os.getcwd(), "output_reports\screenshots\{}".format(filename))
        # element = self.find_element(*locator)

        location = element.location

        _size = self.driver.get_window_size()
        _size = (_size["width"], _size["height"])
        size = element.size

        self.driver.get_screenshot_as_file(filename=screen_shot_path)

        im = Image.open(screen_shot_path)

        _im = im.resize(_size)

        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        _im = _im.crop((left, top, right, bottom))

        _im.save(screen_shot_path)  # saves new cropped image
        # _im.save(screen_shot_path[:-4] + "_element.png")

        print("\n\tPlease see output screenshot: \"{}\".".format(filename))


def get_user(name=None, file_name=r"frontend\program_data\users.csv"):
    try:
        with open(file_name, 'r') as infile:
            reader = csv.DictReader(infile)
            for row in reader:
                user = dict(row)
                if name == user["name"]:
                    return user
    except:
        print("\nUser {} is not defined, enter a valid user.\n".format(name))


def get_input_path_and_file(ext=None, folder="frontend\input_data_sources"):
    _cur_dir = os.path.abspath(os.curdir)
    selected_files = []
    if folder:
        file_path = os.path.join(_cur_dir, folder)
        for _file in os.listdir(file_path):
            if ext and _file.endswith(ext):
                selected_files.append(_file)
            elif not ext and _file.endswith("csv"):
                selected_files.append(_file)
    else:
        file_path = _cur_dir
        for _file in os.listdir(file_path):
            if ext and _file.endswith(ext):
                selected_files.append(_file)
            elif not ext and _file.endswith("csv"):
                selected_files.append(_file)
    return file_path, selected_files


if __name__ == "__main__":
    print(get_user(name="Administrator")["login"])
