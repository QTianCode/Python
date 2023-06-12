"""
  作者：LCQT
  日期：2023年06月10日16:26
  项目描述：Enter键替代鼠标左键
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://baidu.com/')
driver.find_element(By.ID, 'kw').send_keys('洗衣机')
time.sleep(1)
driver.find_element(By.ID, 'kw').send_keys('Keys.ENTER')  # 使用回车键代替鼠标左键
time.sleep(5)