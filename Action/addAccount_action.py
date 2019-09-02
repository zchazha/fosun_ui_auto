from util import page_object

class addAccount():

    @staticmethod
    def add_account(driver):
        try:
            add_account = page_object.Page(driver,"pingtaidai_addAccount_page")
            add_account.get_page_obj("neimao_button").click()
            add_account.get_page_obj("next_step_button").click()
        except Exception as err:
            raise err

if __name__ == "__main__":
    pass


