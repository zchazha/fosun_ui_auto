from util.page_object import Page
import time
from util.parse_mysql import *
class Login():
    @staticmethod
    def login(driver,username,card=None):
        try:
            page =Page(driver,"pingtaidai_login_page")
            # time.sleep(1)
            # page.get_page_obj("username").clear()
            # time.sleep(1)
            # page.get_page_obj("username").send_keys(username)
            page.get_page_obj("password").send_keys("111111")
            page.get_page_obj("login_button").click()
            page.get_page_obj("cash_out_button").click()
            page.get_page_obj("next_step_button").click()
            # page.get_page_obj("finish_button").click()
            page.get_page_obj("bank_list").send_keys("中国工商银行")
            # select = page.get_page_obj("bank_list")
            # print (select)
            # all_options = select.find_elements_by_tag_name("option")
            # for option in all_options:
            #     if u"中国银行" == option.text:
            #         print(u"选项显示的文本：", option.text)
            #         print(u"选项值为：", option.get_attribute("value"))
            #         option.click()
            #         time.sleep(3)
            #     time.sleep(1)
            # page.get_page_obj("")
            page.get_page_obj("card_no").send_keys("6212264100011335373")
            # page.get_page_obj("card_no").send_keys(card)
            page.get_page_obj("contrct").click()
            time.sleep(5)
            page.get_page_obj("argee").click()
            time.sleep(2)
            page.get_page_obj("cash_out_button2").click()
            time.sleep(2)
            page.get_page_obj("send_sms").click()
            time.sleep(2)
            mysql_cofig = ParseCofigFile(parent_dir_path + "\config\\all.ini")
            ip = mysql_cofig.get_option_value("pingtaidai", "mysql_ip")
            db = mysql_cofig.get_option_value("pingtaidai", "mysql_db")
            user = mysql_cofig.get_option_value("pingtaidai", "mysql_username")
            password = mysql_cofig.get_option_value("pingtaidai", "mysql_password")
            mysql = Mysql(ip, user, password, db)
            sql = "select PASSWORD from fc_portal_cust_sms  where MOBILE = '" + username + "' ORDER BY CRT_TIME DESC limit 1;"
            id = mysql.select_data(sql)
            time.sleep(2)
            page.get_page_obj("sms").send_keys(id)
            page.get_page_obj("submit").click()
            time.sleep(2)
            page.get_page_obj("final_finish_button").click()
        except Exception as err:
            raise err
if __name__ == "__main__":
    from Config import var_config
    from selenium import webdriver
    driver = webdriver.Chrome(var_config.chrome75_driver_path)
    driver.get("http://10.166.10.151:38080/credit-portal/login.html")
    Login.login(driver, "13308140486","111111")
