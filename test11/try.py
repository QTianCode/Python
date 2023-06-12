"""
  作者：LCQT
  日期：2023年06月10日18:55
  项目描述：
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 打开Chrome浏览器
driver = webdriver.Chrome()
# 打开网页
driver.get('https://www.wenjuan.com/s/uQzQBv7/')
sleep(1)
name = driver.find_element(By.XPATH, '//*[@id="q_5def9d9d92beb5764c5b2ef4"]/div/div/div/textarea')
name.send_keys("大帅哥")
sleep(5)
name = driver.find_element(By.XPATH, '//*[@id="q_5def9dd23631f2371655e787"]/div[1]/div[2]/input')
name.send_keys("常小宁")
age = driver.find_element(By.XPATH, '//*[@id="q_5def9dd23631f2371655e787"]/div[2]/div[2]/input')
age.send_keys("19岁")
link = driver.find_element(By.XPATH, '//*[@id="q_5def9dd23631f2371655e787"]/div[3]/div[2]/input')
link.send_keys("213000")
# 通过id查找元素
submit = driver.find_element(By.ID, "answer-submit-btn")
sleep(8)
# 单击此元素，提交表单
submit.click()