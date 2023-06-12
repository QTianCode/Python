"""
  作者：LCQT
  日期：2023年06月09日00:05
  项目描述：获取页面标题、URL和浏览器信息
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.bilibili.com/')
# 打印网页标题
print(driver.title)
driver.get('https://www.bilibili.com/')
# 获取当前页面的URL
print(driver.current_url)
driver.get('https://www.bilibili.com/')
# 获取当前浏览器信息
print(driver.capabilities)