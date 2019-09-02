from Config.var_config import upload_file_path
from util.data_provide import DataProvide
from util.page_object import *
import time
from util.log import *
class MyLoan():
    @staticmethod
    def myloan(driver,name,id,live_adderss="户籍居住测试测试地址",qq="123123123",company_name="测试企业名称",company_adderss="企业企业测试测试地址",company_phone="021-88888888",loan_amount="5"):
        try:
            myloan = Page(driver,"pingtaidai_myLoan_page")
            myloan.get_page_obj("name").send_keys(name)
            myloan.get_page_obj("id").send_keys(id)
            #选择婚姻状况
            myloan.get_page_obj("marriage").send_keys("未婚")
            #选择户籍地址
            myloan.get_page_obj("address_live1").send_keys("上海市")
            myloan.get_page_obj("address_live2").send_keys("市辖区")
            myloan.get_page_obj("address_live3").send_keys("黄埔区")
            myloan.get_page_obj("live_adderss").send_keys(live_adderss)
            myloan.get_page_obj("address_is_same").click()
            myloan.get_page_obj("live_prop").click()
            myloan.get_page_obj("education").send_keys("本科")
            myloan.get_page_obj("degree").send_keys("学士")
            myloan.get_page_obj("qq").send_keys(qq)
            myloan.get_page_obj("company_name").send_keys(company_name)
            myloan.get_page_obj("address_company1").send_keys("上海市")
            myloan.get_page_obj("address_company2").send_keys("市辖区")
            myloan.get_page_obj("address_company3").send_keys("黄埔区")
            myloan.get_page_obj("company_adderss").send_keys(company_adderss)
            myloan.get_page_obj("company_phone").send_keys(company_phone)
            myloan.get_page_obj("loan_amount").send_keys(loan_amount)
            myloan.get_page_obj("loan_use").send_keys("备货")
            myloan.get_page_obj("upload_file1").send_keys(upload_file_path+"\\test_pic1.png")
            myloan.get_page_obj("upload_file2").send_keys(upload_file_path+"\\test_pic2.png")
            myloan.get_page_obj("upload_file3").send_keys(upload_file_path+"\\test_pic1.png")
            time.sleep(2)
            myloan.get_page_obj("next_step").click()
            id_flag = 1
            while id_flag:
                if "身份证号输入有误，请重新输入" in driver.page_source:
                    info(id+"身份证号码有误!")
                    id = DataProvide.id()
                    myloan.get_page_obj("id").clear()
                    myloan.get_page_obj("id").send_keys(id)
                    myloan.get_page_obj("next_step").click()
                    id_flag = 1
                else:
                    id_flag = 0

        except Exception as err:
            raise err


if __name__ == "__main__":
    pass



