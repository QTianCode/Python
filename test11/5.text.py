"""
  作者：LCQT
  日期：2023年06月09日00:17
  项目描述：获取元素的文本内容
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = 'https://news.baidu.com/'
driver.get(url)
# 定位
submit = driver.find_element(By.XPATH, "//*[@class='mod-tab-pane active']/div/ul/li[1]/strong/a")  # 定位元素
text = submit.text  # 获取文本信息
print(text)
# //*[@id="pane-news"]