from Config.var_config import parent_dir_path
from util.parse_config import ParseCofigFile
from util.parse_mysql import Mysql


def init_mysql():
    mysql_cofig = ParseCofigFile(parent_dir_path + "\\config\\all.ini")
    ip = mysql_cofig.get_option_value("pingtaidai", "mysql_ip")
    db = mysql_cofig.get_option_value("pingtaidai", "mysql_db")
    username = mysql_cofig.get_option_value("pingtaidai", "mysql_username")
    password = mysql_cofig.get_option_value("pingtaidai", "mysql_password")
    mysql = Mysql(ip, username, password, db)
    return mysql

if __name__ == "__main__":
    mobile=""
    a = init_mysql().select_data('SELECT password from portal.fc_portal_cust_sms  where MOBILE = "13807290003" ORDER BY CRT_TIME DESC limit 1;')
    print (a)