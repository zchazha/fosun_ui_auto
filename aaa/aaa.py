from selenium import webdriver
from Config import var_config
import time

driver = webdriver.Chrome(var_config.chrome75_driver_path)
driver.get("http:\\www.baidu.com")

driver.find_element_by_xpath('//*[@id="kw"]').clear()
# a.send_keys("nihao")
# time.sleep(4)

time.sleep(4)


