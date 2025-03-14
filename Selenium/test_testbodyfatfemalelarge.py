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

class TestTestbodyfatfemalelarge():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testbodyfatfemalelarge(self):
    self.driver.get("https://www.calculator.net/body-fat-calculator.html")
    self.driver.set_window_size(550, 692)
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").click()
    element = self.driver.find_element(By.NAME, "cage")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".cbcontainer:nth-child(2)").click()
    self.driver.find_element(By.NAME, "cage").click()
    self.driver.find_element(By.NAME, "cage").click()
    element = self.driver.find_element(By.NAME, "cage")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "cage").send_keys("1000")
    self.driver.find_element(By.NAME, "cweightkgs").click()
    self.driver.find_element(By.NAME, "cweightkgs").click()
    element = self.driver.find_element(By.NAME, "cweightkgs")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.NAME, "cweightkgs").send_keys("1000")
    self.driver.find_element(By.ID, "cheightmeter").click()
    self.driver.find_element(By.ID, "cheightmeter").click()
    element = self.driver.find_element(By.ID, "cheightmeter")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "cheightmeter").send_keys("1000")
    self.driver.find_element(By.ID, "cneckmeter").click()
    self.driver.find_element(By.ID, "cneckmeter").click()
    element = self.driver.find_element(By.ID, "cneckmeter")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "cneckmeter").send_keys("1000")
    self.driver.find_element(By.ID, "cwaistmeter").click()
    self.driver.find_element(By.ID, "cwaistmeter").click()
    element = self.driver.find_element(By.ID, "cwaistmeter")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "cwaistmeter").send_keys("1000")
    self.driver.find_element(By.ID, "chipmeter").click()
    self.driver.find_element(By.ID, "chipmeter").click()
    element = self.driver.find_element(By.ID, "chipmeter")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.ID, "chipmeter").send_keys("1000")
    self.driver.find_element(By.NAME, "x").click()
    self.driver.find_element(By.CSS_SELECTOR, "font > b").click()
    self.driver.find_element(By.CSS_SELECTOR, "font > b").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "font > b")
    actions = ActionChains(self.driver)
    actions.double_click(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, "font > b").click()
    self.driver.find_element(By.CSS_SELECTOR, ".h2result").click()

    self.driver.find_element(By.NAME, "x").click()
    result_text = self.driver.find_element(By.CSS_SELECTOR, "font > b").text
    assert result_text == "Body Fat: 94.8%"
    print("Female Test Case Result:", result_text)
  
