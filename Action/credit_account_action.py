from util.page_object import *
class CreditAccount():
    @staticmethod
    def credit_account(driver):
        try:
            linkman = Page(driver, "pingtaidai_credit_account_page")
            linkman.get_page_obj("name").send_keys("123123")
            linkman.get_page_obj("password").send_keys("123123")
            linkman.get_page_obj("id").send_keys("123123")
            linkman.get_page_obj("next_step").click()
        except Exception as err:
            raise err
