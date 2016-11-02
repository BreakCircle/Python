#coding=utf-8
from selenium import webdriver

driver=webdriver.Firefox()

driver.get("http://www.baidu.com")

#捕捉百度输入框异常

try:
    driver.find_element_by_id("kwss").send_keys("selenium")
    driver.fing_element_by_id("su").click()
except:
    driver.get_screenshot_as_file("C:\Python27\error.jpg")
driver.quit()
