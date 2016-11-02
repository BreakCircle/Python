# coding=utf-8
from selenium import webdriver
import os
import time
import open_url


sourse = open("E:\\python\\txt.txt", "rb")
values = sourse.readlines()
print values

for s in values:
    driver = webdriver.Firefox()
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").send_keys(s)
    driver.find_element_by_id("su").click()
    driver.quit()


