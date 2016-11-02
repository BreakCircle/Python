#coding=utf-8
from selenium import webdriver
#导入WebDriverWait包
from selenium.webdriver.support.ui import WebDriverWait

#导入时间包
import time

driver = webdriver.Firefox()
driver.get('http://www.baidu.com')

#webdriver用法

element=WebDriverWait(driver,10).until(lambda driver:driver.find_element_by_id('kw'))
element.send_keys('selenium')

#智能等待
driver.implicitly_wait(0.1)
driver.find_element_by_id('su').click()
#休眠时间
time.sleep(5)

driver.quit()
