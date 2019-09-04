from util import page_object
import time
class CoreMakeLoan():

    @staticmethod
    def core_make_loan(driver):
        try:
            page = page_object.Page(driver,"core_make_loan")
            page.get_page_obj("username").send_keys("88888888")
            page.get_page_obj("password").send_keys("88888888")
            page.get_page_obj("login_button").click()
            time.sleep(3)
            page.get_page_obj("loan_manage").click()
            time.sleep(2)
            page.get_page_obj("loan_approve_button").click()
            time.sleep(3)
            driver.switch_to.frame(driver.find_element_by_id("201701040950530004000000000140"))
            page.get_page_obj("new_tast_button").click()
            time.sleep(2)
            page.get_page_obj("receive_task_button").click()
            time.sleep(3)
            page.get_page_obj("confirm_button").click()
            time.sleep(4)
            page.get_page_obj("flow_info_button").click()
            time.sleep(2)
            page.get_page_obj("approve_opinion").send_keys("放款通过！")
            time.sleep(2)
            page.get_page_obj("submit_opinion_button").click()
            time.sleep(4)
            page.get_page_obj("confirm2_button").click()

        except Exception as err:
            raise err

if __name__ == "__main__":
    from Config import var_config
    from selenium import webdriver
    driver = webdriver.Chrome(var_config.chrome75_driver_path)
    url = "http://" +"10.166.10.151" + ":18082/authority-app/scube_ui/login_module/html/login.html"
    driver.get(url)
    CoreMakeLoan.core_make_loan(driver)
    print("放款成功")