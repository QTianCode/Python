"""
  作者：LCQT
  日期：2023年06月10日15:59
  项目描述：运用鼠标对元素拖拽
"""
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
try:
    driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    driver.maximize_window()
    driver.switch_to.frame('iframeResult')
    source = driver.find_element(By.ID, 'draggable')
    # 定位到拖拽起始点
    target = driver.find_element(By.ID, 'droppable')
    # 定位到拖拽目标点
    print(source)
    print(target)
    # actions = ActionChains(driver)
    # actions.drag_and_drop(source, target)
    # actions.perform()
    ActionChains(driver).drag_and_drop(source, target).perform()
    time.sleep(5)
except Exception as e:
    print(e)
finally:
    driver.quit()