from Config.var_config import upload_file_path
from util.page_object import Page
import time
class CorePreApprove():

    @staticmethod
    def core_pre_approve(driver):
        try:
            page = Page(driver,"core_pre_approve")
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
            page.get_page_obj("thrid_info_button").click()
            page.get_page_obj("receive_report_button").click()
            page.get_page_obj("click_simple_report_button").click()
            page.get_page_obj("choice_file").send_keys(upload_file_path+"\\刘荣真.pdf")
            page.get_page_obj("receive_file_button").click()
            page.get_page_obj("confirm_button1").click()
            time.sleep(2)
            page.get_page_obj("flow_info_button").click()
            page.get_page_obj("agree_button").click()
            page.get_page_obj("approve_opinion").send_keys("审批通过")
            page.get_page_obj("submit_opinion_button").click()
            time.sleep(5)
            page.get_page_obj("confirm2_button").click()
            time.sleep(2)

        except Exception as err:
            raise err




