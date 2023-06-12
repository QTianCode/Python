"""
  作者：LCQT
  日期：2023年06月08日15:48
  项目描述：
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 打开Chrome浏览器
driver = webdriver.Chrome()
# 打开网页
driver.get('https://www.wenjuan.com/s/UZBZJvoVFN/?share_device=qq')
sleep(1)
# 通过class_name查找元素
name = driver.find_element(By.XPATH, '//*[@id="q_61bb311667864f977be5f812"]/div/div/div/textarea')
name.send_keys("大帅哥")
sleep(1)
score = driver.find_element(By.XPATH, '//*[@id="q_61bb312367864f977be5f815"]/div/div/div/textarea')
score.send_keys('525134')
sleep(3)

# 选择题
elem = driver.find_elements(By.XPATH, '//*[@id="question-61bb315e67864f9775eeefc4"]/div[2]/div[1]/div/div')
elem[0].click()
sleep(1)

# 最后一题
last = driver.find_elements(By.XPATH, '//*[@id="question-61bb319d6b9359702e771130"]/div[2]/div[1]/div/div')
elem[1].click()
sleep(3)