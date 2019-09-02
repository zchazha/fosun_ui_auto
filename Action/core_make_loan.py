from util import page_object
class CoreMakeLoan():

    @staticmethod
    def Core_make_loan(driver):
        try:
            add_account = page_object.Page(driver,"core_login")
            add_account.get_page_obj("username").send_keys("88888888")
            add_account.get_page_obj("password").send_keys("88888888")
            add_account.get_page_obj("login_button").click()
        except Exception as err:
            raise err

if __name__ == "__main__":
    pass