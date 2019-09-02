import os
# 获取当前文件所在目录的父目录的绝对路径
parent_dir_path = os.path.dirname(os.path.dirname(__file__))
# 获取存放页面元素定位表达式文件的绝对路径
page_element_locator_path = parent_dir_path + "\\config\\page_element_locator.ini"
#获取图片所有的绝对路径
upload_file_path = parent_dir_path + "\\UploadFile"
#chrome75驱动地址
chrome75_driver_path  = parent_dir_path +"\\BrowserDriver\chrome75\chromedriver"
#配置文件的位置
all_config_dir_path = parent_dir_path + "\\config\\all.ini"

