"""
  作者：LCQT
  日期：2023年06月08日16:44
  项目描述：每种定位要单独实现
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get('https://www.baidu.com/')
# 通过id定位
# driver.find_element(By.ID, "s-usersetting-top").click()  # 单击“设置”按钮
# time.sleep(5)

# 通过元素name定位
# driver.find_element(By.NAME,"wd").send_keys("python1+X")   # 在搜索框输入 1+X
# time.sleep(5)

# 通过class_name定位
# driver.find_element(By.CLASS_NAME,"s-top-login-btn").click()  # 单击“登录”按钮
# time.sleep(5)

# 通过元素tag_name定位
# driver.find_element(By.TAG_NAME, "p")[0].click()
# 定位标签为<p>的元素，并单击
#time.sleep(5)
# 通过链接文本定位
# 通过元素链接全部文本来定位元素，单击“使用百度前必读”
#driver.find_element(By.LINK_TEXT, '登录').click()
# 通过元素链接部分文本来定位元素，单击“使用百度前必读”
# driver.find_element_by_partial_link_text("使用百度前必读").click()
driver.find_element(By.XPATH,"//*[@class='bg s_btn']")
time.sleep(5)
# 退出驱动器
driver.quit()