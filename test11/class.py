"""
  作者：LCQT
  日期：2023年06月09日23:59
  项目描述：
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.set_page_load_timeout(30)
driver.get('https://search.jd.com/search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&ev=exbrand_%E5%8D%8E%E7%A1%95%EF%BC%88ASUS%EF%BC%89%5E')
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')  # 滚动屏幕
time.sleep(3)

goods = driver.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li')
print('本页共有商品：',len(goods),'件')
for good in goods:
    try:
        title = good.find_element(By.XPATH, './div/div[3]/a/em').text
        price = good.find_element(By.XPATH, './div/div[2]/strong/i').text
        print(title, price)
    except Exception as e:
        print(e)

driver.quit()


