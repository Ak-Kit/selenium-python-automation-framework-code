import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def page_scroll(self):
        # To handle Dynamic Scrolling
        pagelength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);var pageLength=document.body.scrollHeight")
        match = False
        while (match == False):
            lastCount = pagelength
            time.sleep(2)
            lenOfPage = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);var pagelength= document.body.scrollHeight")
            if lastCount == pagelength:
                match = True

        time.sleep(6)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        list_of_elements = wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_elements_is_clickable(self, locator_type, locator):
        wait = WebDriverWait(self.driver, 10)
        element= wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element


    def test_method(self):
        print("Test Merge")

    def test_method_sdet1(self):
        print("SDET1 Test Merge")