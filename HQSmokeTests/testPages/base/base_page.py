import time
import datetime

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from HQSmokeTests.userInputs.user_inputs import UserData

"""This class contains all the generic methods and utilities for all pages"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_to_click(self, locator, timeout=10):
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).click()

    def wait_to_clear(self, locator, timeout=5):
        clickable = ec.visibility_of_element_located(locator)
        WebDriverWait(self.driver, timeout).until(clickable).clear()

    def wait_to_send_keys(self, locator, user_input):
        clickable = ec.visibility_of_element_located(locator)
        WebDriverWait(self.driver, 5).until(clickable).send_keys(user_input)

    def wait_to_get_text(self, locator, timeout=20):
        clickable = ec.visibility_of_element_located(locator)
        element_text = WebDriverWait(self.driver, timeout).until(clickable).text
        return element_text

    def wait_for_element(self, locator, timeout=20):
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable)

    def wait_and_sleep_to_click(self, locator, timeout=20):
        time.sleep(4)
        clickable = ec.element_to_be_clickable(locator)
        WebDriverWait(self.driver, timeout).until(clickable).click()

    def click(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def clear(self, locator):
        element = self.driver.find_element(*locator)
        element.clear()

    def send_keys(self, locator, user_input):
        element = self.driver.find_element(*locator)
        element.send_keys(user_input)

    def get_text(self, locator):
        element = self.driver.find_element(*locator)
        element_text = element.text
        print(element_text)
        return element_text

    def get_attribute(self, locator, attribute):
        element = self.driver.find_element(*locator)
        element_attribute = element.get_attribute(attribute)
        print(element_attribute)
        return element_attribute

    def is_visible_and_displayed(self, locator, timeout=20):
        visible = ec.visibility_of_element_located(locator)
        element = WebDriverWait(self.driver, timeout).until(visible, message="Element not displayed")
        return bool(element)

    def is_present_and_displayed(self, locator, timeout=60):
        visible = ec.presence_of_element_located(locator)
        element = WebDriverWait(self.driver, timeout).until(visible, message="Element not displayed")
        return bool(element)

    def switch_to_next_tab(self):
        winHandles = self.driver.window_handles
        window_after = winHandles[1]
        self.driver.switch_to.window(window_after)

    def switch_to_new_tab(self):
        self.driver.switch_to.new_window('tab')

    def switch_back_to_prev_tab(self):
        winHandles = self.driver.window_handles
        window_before = winHandles[0]
        self.driver.switch_to.window(window_before)

    def get_environment(self):
        get_env = self.driver.current_url
        env_name = get_env.split("/")[2]
        print("server : " + env_name)
        return env_name

    def get_domain(self):
        get_url = self.driver.current_url
        domain_name = get_url.split("/")[4]
        print("domain: " + domain_name)
        return domain_name

    def assert_downloaded_file(self, newest_file, file_name):
        modTimesinceEpoc = (UserData.DOWNLOAD_PATH / newest_file).stat().st_mtime
        modificationTime = datetime.datetime.fromtimestamp(modTimesinceEpoc)
        timeNow = datetime.datetime.now()
        diff_seconds = round((timeNow - modificationTime).total_seconds())
        print("Last Modified Time : ", str(modificationTime) + 'Current Time : ', str(timeNow),
              "Diff: " + str(diff_seconds))
        assert file_name in newest_file and diff_seconds in range(0, 600), "Export not completed"
