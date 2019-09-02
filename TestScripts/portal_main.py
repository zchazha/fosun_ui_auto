from selenium import webdriver

from Action.core_login import CoreLogin
from Action.core_pre_approve import CorePreApprove
from Action.core_junior_approve import CoreJuniorApprove
from Action.core_final_approve import CoreFinalApprove
from Action.credit_account_action import CreditAccount
from Action.login_action import Login
from Action.init_mysql_action import init_mysql
from Action.linkman_action import Linkman
from Action.addAccount_action import addAccount
from Action.register_action import Register
from Action.myloan_action import *
from Config import var_config
from util.data_provide import DataProvide
import time
from util.log import *
import logging

driver = webdriver.Chrome(var_config.chrome75_driver_path)
ip = ParseCofigFile(var_config.all_config_dir_path).get_option_value("pingtaidai", "ip")
card = DataProvide.bank_account()
mobile = ""
def excete_portal_action():
    global mobile
    url = "http://" + ip + ":38080/credit-portal/register.html"
    driver.get(url)
    # driver.maximize_window()
    mobile = DataProvide.phone()
    info("手机号："+str(mobile))
    #注册
    Register.register(driver,mobile ,"111111")
    time.sleep(2)
    #插入天猫数据
    cust_no_sql = "SELECT CUST_NO FROM fc_portal_cust_register WHERE MOBILE = '"+mobile+"'"
    cust_no = init_mysql().select_data(cust_no_sql)
    insert_sql = "INSERT INTO fc_portal_cust_domestic_trade VALUES ('%s.012100ID73619', '%s', " \
                 "'156662686', '-', '3', '1', 'moderntwist旗舰店','320594000201512000000','%s','%s'," \
                 "'天猫卖家首页信息加载完毕！', 'TM','YTXD20180829100518TMYTXD0000001');" % (
                 int(time.time()), cust_no, time.strftime('%Y-%m-%d %H:%M:%S'), time.strftime('%Y-%m-%d %H:%M:%S'))
    init_mysql().insert_data(insert_sql)
    time.sleep(2)
    #添加电商账号
    addAccount.add_account(driver)
    time.sleep(2)
    #申请人信息
    name = DataProvide.name()
    id = DataProvide.id()
    MyLoan.myloan(driver,name,id)
    info("姓名："+name)
    info("身份证号："+ id)
    info("申请人页面申请成功")
    time.sleep(2)
    #联系人账户
    Linkman.linkman(driver)
    info("联系人页面成功")
    time.sleep(2)
    #征信账户
    CreditAccount.credit_account(driver)
    time.sleep(5)
    assert u"恭喜,申请提交成功!" in driver.page_source
    info("portal端成功！")

def core_action():
    url = "http://" + ip + ":18082/authority-app/scube_ui/login_module/html/login.html"
    driver.get(url)
    driver.maximize_window()
    CoreLogin.core_login(driver)
    time.sleep(3)
    CorePreApprove.core_pre_approve(driver)
    info("预审成功！")
    CoreJuniorApprove.core_junior_approve(driver)
    info("初审成功！")
    CoreFinalApprove.core_final_approve(driver)
    info("终审审成功！")

def login():
    url = "http://" + ip + ":38080/credit-portal/login.html"
    driver.get(url)
    driver.maximize_window()
    time.sleep(20)
    Login.login(driver,mobile,card)
    info("提现成功！")
def quit():
    driver.quit()

if __name__ == "__main__":
    # for i in range(10):
    #     excete_portal_action()
    # quit()
    excete_portal_action()
    core_action()
    login()
    quit()


