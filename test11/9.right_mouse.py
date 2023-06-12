"""
  作者：LCQT
  日期：2023年06月10日15:43
  项目描述：右击鼠标
"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# 定位到要右击的元素
right_click = driver.find_element(By.ID, 'head_wrapper')
# 对定位到的元素执行鼠标右键操作
ActionChains(driver).context_click(right_click).perform()
time.sleep(5)
