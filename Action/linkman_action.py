from util.page_object import *
class Linkman():
    @staticmethod
    def linkman(driver):
        try:
            linkman = Page(driver,"pingtaidai_linkman_page")
            linkman.get_page_obj("home_link_name").send_keys("家庭联系人")
            linkman.get_page_obj("home_link_phone").send_keys("13410010001")
            linkman.get_page_obj("work_link_name").send_keys("工作联系人")
            linkman.get_page_obj("work_link_phone").send_keys("13410010002")
            linkman.get_page_obj("other_link_name").send_keys("其它联系人")
            linkman.get_page_obj("other_link_phone").send_keys("13410010003")
            linkman.get_page_obj("next_step").click()
        except Exception as err:
            raise err