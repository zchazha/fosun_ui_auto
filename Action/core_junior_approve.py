from util.page_object import Page
import time
class CoreJuniorApprove():
    @staticmethod
    def core_junior_approve(driver):
        try:
            page = Page(driver,"core_junior_approve")
            # driver.switch_to.frame(driver.find_element_by_id("201701040950530004000000000140"))
            page.get_page_obj("task_receive").click()
            time.sleep(2)
            page.get_page_obj("new_tast_button").click()
            time.sleep(2)
            page.get_page_obj("receive_task_button").click()
            time.sleep(2)
            page.get_page_obj("confirm_button").click()
            time.sleep(2)
            page.get_page_obj("liangfu_query_button").click()
            time.sleep(2)
            page.get_page_obj("choice_liangfu_report").click()
            time.sleep(2)
            page.get_page_obj("choice_specfic_report").click()
            time.sleep(2)
            page.get_page_obj("comfirm_button").click()
            time.sleep(2)
            page.get_page_obj("score_model").click()
            time.sleep(3)
            page.get_page_obj("flow_info_button").click()
            time.sleep(2)
            page.get_page_obj("agree_button").click()
            time.sleep(2)
            page.get_page_obj("approve_opinion").send_keys("初审同意！")
            time.sleep(2)
            page.get_page_obj("submit_opinion_button").click()
            time.sleep(5)
            page.get_page_obj("confirm2_button").click()

        except Exception as err:
            raise err
