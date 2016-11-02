from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chaims import ActionChains

m=driver.find_element_by_xpath("//div[@id='zhng']")
target=driver.find_element_by_xpatn("/html/body/div[3]/input")

ActionChains(driver).right_context(m).perform()
ActionChains(driver).double_click(m).perform()
ActionChains(driver).drag_and_drop(m,target).perform()
ActionChains(driver).move_to_element(a,target).perform()
