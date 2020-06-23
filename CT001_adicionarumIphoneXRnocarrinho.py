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

class TestAdicionarumIphoneXRnocarrinho():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_adicionarumIphoneXRnocarrinho(self):
    self.driver.get("https://www.casasbahia.com.br/")
    self.driver.set_window_size(738, 670)
    self.driver.find_element(By.ID, "strBusca").click()
    self.driver.find_element(By.ID, "strBusca").send_keys("iphone xr")
    self.driver.find_element(By.CSS_SELECTOR, ".ac-hover > .ac-product-name").click()
    self.driver.find_element(By.ID, "btnAdicionarCarrinho").click()
    element = self.driver.find_element(By.LINK_TEXT, "Continuar")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Continuar").click()
  
