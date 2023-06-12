"""
  作者：LCQT
  日期：2023年06月10日17:07
  项目描述：提交表单
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 打开Chrome浏览器
driver = webdriver.Chrome()
# 打开网页
driver.get('https://www.wenjuan.com/s/uQzQBv7/')
sleep(1)
# 通过class_name查找元素
elem_radio = driver.find_elements(By.CLASS_NAME, "question-box")
sleep(1)
# 单击第一个选项
elem_radio[0].click()
sleep(1)
elem_radio[3].click()
# 选中第1、2、4个选项
elem_check = driver.find_elements(By.CLASS_NAME, "question-box")
elem_check[0].click()
elem_check[1].click()
elem_check[3].click()
# 查找下拉框按钮，单击第一个元素‘应该不会留’
elem_wapper = driver.find_elements(By.CLASS_NAME, "w-selection-wrapper")
elem_wapper[0].click()
# 找到所有选项，单击第三个元素‘可能会留’
option_cell = driver.find_elements(By.CLASS_NAME, "w-selection-option")
option_cell[2].click()
# 通过id查找元素
textarea = driver.find_elements(By.ID, "5def9d9d92beb5764c5b2ef4")
# send_keys可以发送内容和操作
textarea.send_keys("晴空万里")
# 通过class_name查找元素
score = driver.find_elements(By.CLASS_NAME, "div_float");
# 打四颗星
score[3].click()
# 通过id查找元素，输入名字、年龄、号码
name = driver.find_element(By.ID, "option_5def9dd23631f2371655e788")
name.send_keys("常小宁")
age = driver.find_element(By.ID, 'option_5def9dd23631f2371655e789')
age.send_keys("19岁")
link = driver.find_element(By.ID,'option_5def9dd23631f2371655e78a')
link.send_keys("213000")
# 通过id查找元素
submit = driver.find_element(By.ID, "next_button")
sleep(8)
# 单击此元素，提交表单
submit.click()
