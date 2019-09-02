#encoding=utf-8
from configparser import ConfigParser

from Config.var_config import parent_dir_path

class ParseCofigFile(object):

    def __init__(self,config_path):
        self.cf = ConfigParser()
        # self.cf.read(pageElementLocatorPath, encoding="utf-8-sig")
        # 如果配置文件中存在中文，以utf-8编码读取
        self.cf.read(config_path, encoding="utf-8")

    def get_items_section(self, section_name):
        # 获取配置文件中指定section下的所有option键值对
        # 并以字典类型返回给调用者
        """注意：
        使用self.cf.items(sectionName)此种方法获取到的
        配置文件中的options内容均被转换成小写，
        比如：loginPage.frame被转换成了loginpage.frame
        """
        options_dict = dict(self.cf.items(section_name))
        return options_dict

    def get_option_value(self, section_name, option_name):
        # 获取指定section下的指定option的值
        value = self.cf.get(section_name, option_name)
        return value

if __name__ == '__main__':
    # pc = ParseCofigFile(parent_dir_path+"\config\\all.ini")
    pc = ParseCofigFile(parent_dir_path+"\config\\page_element_locator.ini")
    print(pc.get_option_value("pingtaidai_register_page", "mobile_input"))