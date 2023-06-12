"""
  作者：LCQT
  日期：2023年06月09日00:11
  项目描述：获取元素尺寸
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('https://www.bilibili.com/')
# 定位输入框
input_box = driver.find_element(By.ID,"nav-searchform")
# 打印输入框尺寸
print(input_box.size)