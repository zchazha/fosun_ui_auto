from util.page_object import Page
import time

class CoreFinalApprove():
    @staticmethod
    def core_final_approve(driver,loan_term = "loan_plan_12"):
        try:
            page = Page(driver,"core_final_approve")
            time.sleep(2)
            page.get_page_obj("task_receive").click()
            time.sleep(2)
            page.get_page_obj("new_tast_button").click()
            time.sleep(4)
            page.get_page_obj("receive_task_button").click()
            time.sleep(3)
            page.get_page_obj("confirm_button").click()
            time.sleep(2)
            page.get_page_obj("aprrove_confirm_info_button").click()
            time.sleep(2)
            # 选择S
            # page.get_page_obj("final_level").click()
            # time.sleep(2)
            page.get_page_obj(loan_term).click()
            time.sleep(2)
            page.get_page_obj("save").click()
            time.sleep(3)
            page.get_page_obj("confirm").click()
            time.sleep(2)
            page.get_page_obj("flow_info_button").click()
            time.sleep(2)
            page.get_page_obj("agree_button").click()
            time.sleep(2)
            page.get_page_obj("approve_opinion").send_keys("终审通过！")
            page.get_page_obj("submit_opinion_button").click()
            time.sleep(5)
            page.get_page_obj("confirm2_button").click()
        except Exception as err:
            raise err