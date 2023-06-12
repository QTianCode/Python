"""
  作者：LCQT
  日期：2023年06月10日15:19
  项目描述：获取属性值
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)
for link in driver.find_elements(By.XPATH, "//*[@href]"):
    print(link.get_attribute('href'))
