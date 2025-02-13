import os
import time
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

from base_pages.home_page import Home_Page


class Test_search_result:
    home_page_url = "https://www.practo.com/"
    location = 'Pune hinjewadi'
    doctor = 'Dentist'

    def test_homePage_title_verification(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.home_page_url)
        actual_title = self.driver.title
        expected_title = "Practo | Video Consultation with Doctors, Book Doctor Appointments, Order Medicine, Diagnostic Tests"

        if actual_title == expected_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()
            assert False

    def test_search_functionality(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.home_page_url)

        self.home_search = Home_Page(self.driver)
        self.home_search.search_location(self.location)
        self.home_search.search_doctor(self.doctor)
        time.sleep(2)

        actual_title = self.driver.find_element(By.XPATH, "//p[@class='u-x-large-font']").text
        expected_title = "Book appointments with minimum wait-time & verified doctor details"

        #actual_title = self.driver.title
        #expected_title = "Find Best Dentists in Pune on Practo. Book Instant Appointments ,View Fees, Reviews & Contact Details.


        print(f"Matched Actual and Expected Title: {actual_title}")
        if actual_title == expected_title:
            assert True
            self.driver.close()
        else:
            # Ensure the screenshots directory exists
            screenshot_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)

            # Save screenshot with correct path
            screenshot_path = os.path.join(screenshot_dir, "test_search_functionality.png")
            self.driver.save_screenshot(screenshot_path)
            self.driver.close()
            assert False,  f"Title mismatch! Expected: {expected_title}, but got: {actual_title}"

