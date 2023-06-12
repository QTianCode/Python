"""
  作者：LCQT
  日期：2023年06月08日18:18
  项目描述：
"""
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# 用XPath通过id属性定位
# driver.find_element(By.XPATH, "//*[@id='kw']").send_keys("python1+X")

# 用XPath通过name属性定位
# driver.find_element(By.XPATH, "//*[@name='wd']").send_keys("python1+X")

# 用Xpath通过层级定位
driver.find_element(By.XPATH, "//form[@id='form']/span/input").send_keys("python1+X")
time.sleep(5)
driver.quit()
