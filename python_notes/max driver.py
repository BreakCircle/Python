#coding=utf-8
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")

print "浏览器最大化"
driver.maximize_window()  #最大化浏览器
driver.quit()
