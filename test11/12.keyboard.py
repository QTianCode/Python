"""
  作者：LCQT
  日期：2023年06月10日16:08
  项目描述：键盘操作
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://baidu.com/')
putkeys = driver.find_element(By.ID, 'kw')
baidu = driver.find_element(By.ID, 'su')
putkeys.send_keys("python1+X")
baidu.click()
time.sleep(4)
driver.quit()