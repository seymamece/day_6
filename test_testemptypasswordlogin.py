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
from webdriver_manager.chrome import ChromeDriverManager

class TestTestemptypasswordlogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome(ChromeDriverManager().install())
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testemptypasswordlogin(self):
    self.driver.get("https://www.saucedemo.com/")
    self.driver.maximize_window()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("Meryem")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("standard_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"username\"]").send_keys("problem_user")
    self.driver.find_element(By.CSS_SELECTOR, "*[data-test=\"login-button\"]").click()
  
