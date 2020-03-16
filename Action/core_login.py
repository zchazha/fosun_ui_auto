from util import page_object
class CoreLogin():

    @staticmethod
    def core_login(driver):
        try:
            add_account = page_object.Page(driver,"core_login")
            add_account.get_page_obj("username").send_keys("zhouxx")
            add_account.get_page_obj("password").send_keys("QQQwww111222")
            add_account.get_page_obj("login_button").click()
        except Exception as err:
            raise err

if __name__ == "__main__":
    pass