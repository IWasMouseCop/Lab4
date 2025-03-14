# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestbodyfatmaleinvalid():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testbodyfatmaleinvalid(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(550, 692)
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").send_keys("0")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("0")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("0")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("0")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("0")
    self.driver.find_element(By.NAME, "x").click()

    self.driver.find_element(By.NAME, "x").click()
    result_text = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
    assert result_text == "Body Fat: 15.7%"
    print("Male Test Case Result:", result_text)
  
