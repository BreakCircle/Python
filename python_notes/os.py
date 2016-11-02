#coding=utf-8

from selenium import webdriver
import os

driver=webdriver.Firefox()
file_path="file:///"+os.path.abspath("checkbox.html")
file_path="file:///"+os.path.abspath("checkbox.html")

driver.get(file_path)

#找出tag为input的元素
inputs=driver.find_elements_by_tag_name("input")

#找出type为checkbox的元素 单击

for input in inputs:
    if input.get_attribute("type")=="checkbox":
        input.click()

driver.quit()
