"""
  作者：LCQT
  日期：2023年06月10日15:53
  项目描述：移动鼠标
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.jd.com/')
e = driver.find_element(By.LINK_TEXT, '工业品')
# 将鼠标悬停在工业品上，暂停0.1s,并点击
ActionChains(driver).move_to_element(e).pause(0.1).click(e).perform()
time.sleep(5)
