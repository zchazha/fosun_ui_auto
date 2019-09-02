#encdoing = utf-8
from selenium import webdriver

from Config import var_config
from util.parse_mysql import *
from util import page_object
import time
class Register():

    @staticmethod
    def register(driver,mobile,passward):
        try:
            register = page_object.Page(driver,"pingtaidai_register_page")
            register.get_page_obj("mobile").send_keys(mobile)
            register.get_page_obj("id_button").click()
            #数据库查询验证码
            mysql_cofig = ParseCofigFile(parent_dir_path + "\config\\all.ini")
            ip = mysql_cofig.get_option_value("pingtaidai", "mysql_ip")
            db = mysql_cofig.get_option_value("pingtaidai", "mysql_db")
            username = mysql_cofig.get_option_value("pingtaidai", "mysql_username")
            password = mysql_cofig.get_option_value("pingtaidai", "mysql_password")
            mysql = Mysql(ip, username, password, db)
            sql = "SELECT password from portal.fc_portal_cust_sms  where MOBILE = '" + mobile + "' ORDER BY CRT_TIME DESC limit 1;"
            id = mysql.select_data(sql)
            # 固定验证码
            # id = "123456"
            register.get_page_obj("id").send_keys(id)
            register.get_page_obj("password").send_keys(passward)
            register.get_page_obj("register_button").click()
            if "验证码错误" in driver.page_source:
                id = "123456"
                register.get_page_obj("id").clear()
                time.sleep(2)
                register.get_page_obj("id").send_keys(id)
                time.sleep(2)
                register.get_page_obj("register_button").click()

        except Exception as err:
            raise err

if __name__ == "__main__":

    driver = webdriver.Chrome(parent_dir_path+"\\BrowserDriver\\chrome75\\chromedriver")
    ip = ParseCofigFile(var_config.all_config_dir_path).get_option_value("pingtaidai","ip")
    url = "http://" + ip + ":38080/credit-portal/register.html"
    driver.get(url)
    Register.register(driver,"13807300099","111111")
    # time.sleep(5)
    # driver.quit()





