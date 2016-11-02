# coding=utf-8
from selenium import webdriver

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
#最大化窗口
print "窗口最大化"
driver.maximize_window()
<a href="http://www.zhidao.baidu.com" name="tj_zhidao">知道</a>
find_element_by_link_text("知道")
find_element_by_partial_link_text("知道")
