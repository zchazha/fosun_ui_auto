from selenium.webdriver.support.wait import WebDriverWait
from Config.var_config import page_element_locator_path
from util.parse_config import *

class Page():
    def __init__(self,driver,section,path= page_element_locator_path):
        self.driver = driver
        self.parser_cf = ParseCofigFile(path)
        self.register_options = self.parser_cf.get_items_section(section)

    def get_element(self,locate_type, locator_expression):
        try:
            element = WebDriverWait(self.driver, 30).until \
                (lambda x: x.find_element(by=locate_type, value=locator_expression))
            return element
        except Exception as err:
            raise err

    # 获取多个相同页面元素对象，以list返回
    def get_elements(self,locate_type, locator_expression):
        try:
            elements = WebDriverWait(self.driver, 30).until(
                lambda x: x.find_elements(by=locate_type, value=locator_expression))
            return elements
        except Exception as err:
            raise err

    def get_page_obj(self,key):
        try:
            locate_type, locator_expression = self.register_options[key].split(">")
            element_obj = self.get_element(locate_type, locator_expression)
            return element_obj
        except Exception as err:
            raise err

if __name__ == "__main__":
    from selenium import webdriver
    import os
    driver_path  = os.path.dirname(os.path.dirname(__file__))+"\\BrowserDriver\chrome75\chromedriver"
    driver = webdriver.Chrome(executable_path =driver_path)
    driver.get("http://10.166.10.136:38080/credit-portal/register.html")
    page = Page(driver,"pingtaidai_register_page")
    mobile = page.get_page_obj('mobile')
    mobile.send_keys("121212")