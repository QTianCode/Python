"""
  作者：LCQT
  日期：2023年06月10日15:28
  项目描述：鼠标操作
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 打开新浪注册页面
driver.get('https://login.sina.com.cn/signup/signup?entry=homepage')
# 从浏览器开发者工具中直接复制“新闻”复选框的CSS选择器路径
news_css = '#phone-form > div.info_list.clearfix.fav_tags > div.ipt.checklst > label:nth-child(9) > input'
# 定位到“新闻”复选框
ck_news = driver.find_element(By.CSS_SELECTOR, news_css)
# 单击“新闻”复选框，获得初始节点位置
# 依次实现动作链：首先移动到“新闻”，然后单击，最后执行
ActionChains(driver).move_to_element(ck_news).click().perform()
time.sleep(5)
driver.quit()