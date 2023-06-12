"""
  作者：LCQT
  日期：2023年06月09日00:33
  项目描述：
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = 'https://new.qq.com/'
driver.get(url)
# 定位
submit = driver.find_element(By.XPATH, "//*[@id='qqcom-rankWrap']/ul/li[1]/a")  # 定位元素
text = submit.text  # 获取文本信息
print(text)
