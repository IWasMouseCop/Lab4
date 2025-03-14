
# Generated by Selenium IDE
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestBodyFatCalculator:
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.set_window_size(1936, 1048)

    def teardown_method(self, method):
        self.driver.quit()

    def test_body_fat_male(self):
        # Navigate to Body Fat Calculator
        self.driver.get("https://www.calculator.net/body-fat-calculator.html")

        # Locate the Male radio button
        male_radio = self.driver.find_element(By.ID, "csex1")

        # Use JavaScript to click on the Male radio button
        self.driver.execute_script("arguments[0].click();", male_radio)

        # Continue with the rest of the test steps
        self.driver.find_element(By.NAME, "cage").clear()
        self.driver.find_element(By.NAME, "cage").send_keys("25")
        self.driver.find_element(By.NAME, "cweightkgs").clear()
        self.driver.find_element(By.NAME, "cweightkgs").send_keys("70")
        self.driver.find_element(By.ID, "cheightmeter").clear()
        self.driver.find_element(By.ID, "cheightmeter").send_keys("178")
        self.driver.find_element(By.ID, "cneckmeter").clear()
        self.driver.find_element(By.ID, "cneckmeter").send_keys("50")
        self.driver.find_element(By.ID, "cwaistmeter").clear()
        self.driver.find_element(By.ID, "cwaistmeter").send_keys("96")

        # Calculate and verify the result
        self.driver.find_element(By.NAME, "x").click()
        result_text = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
        assert result_text == "Body Fat: 15.7%"
        print("Male Test Case Result:", result_text)
