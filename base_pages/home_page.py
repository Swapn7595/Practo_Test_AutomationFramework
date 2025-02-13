
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By


class Home_Page:
    searchbox_location_xpath = "//input[@data-input-box-id = 'omni-searchbox-locality']"
    searchbox_doctor_xpath = "//input[@data-input-box-id = 'omni-searchbox-keyword']"

    def __init__(self, driver):
        self.driver = driver

    def search_location(self, location):
        search_box_location = self.driver.find_element(By.XPATH, self.searchbox_location_xpath)
        search_box_location.clear()
        search_box_location.send_keys(location)

        search_box_doctor = self.driver.find_element(By.XPATH, self.searchbox_doctor_xpath).click()
        #search_box_location.send_keys(keys.RETURN)

    def search_doctor(self, doctor):
        search_box_doctor = self.driver.find_element(By.XPATH, self.searchbox_doctor_xpath)
        search_box_doctor.clear()
        search_box_doctor.send_keys(doctor)
        search_box_doctor.send_keys(Keys.RETURN)
