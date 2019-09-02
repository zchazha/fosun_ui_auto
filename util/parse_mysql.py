# encoding=utf-8
import pymysql
from util.parse_config import ParseCofigFile
from Config.var_config import parent_dir_path
class Mysql():
    def __init__(self,host,user,passwd,db=None):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.db = db
        self.conn = pymysql.connect(
            host=self.host,
            port=3306,
            user=self.user,
            passwd=self.passwd,
            db=self.db,
            charset="utf8")
        self.cur = self.conn.cursor()

    def select_data(self,select_sql):
        # self.conn.select_db(self.db)
        self.cur.execute(select_sql)
        result = self.cur.fetchone()
        return result[0]
        self.conn.commit()
        self.conn.close()

    def insert_data(self,insert_sql):
        try:
            # 执行SQL语句
            self.cur.execute(insert_sql)
            # 提交到数据库执行
            self.conn.commit()
        except:
            # 发生错误时回滚
            self.conn.rollback()
        self.cur.close()
        self.conn.close()

if "__name == __main__":
    pass
    # mysql_cofig = ParseCofigFile(parent_dir_path + "\config\\all.ini")
    # ip = mysql_cofig.get_option_value("pingtaidai","mysql_ip")
    # db = mysql_cofig.get_option_value("pingtaidai", "mysql_db")
    # username = mysql_cofig.get_option_value("pingtaidai", "mysql_username")
    # password = mysql_cofig.get_option_value("pingtaidai", "mysql_password")
    # mysql = Mysql(ip,username,password,db)
    # username = "13308140486"
    # sql = "select PASSWORD from fc_portal_cust_sms  where MOBILE = '" + username + "' ORDER BY CRT_TIME DESC limit 1;"
    # id = mysql.select_data(sql)
    # print (id)

    # insert_sql = "INSERT INTO fc_portal_cust_domestic_trade VALUES ('%s.012100ID73619', '%s', " \
    #          "'156662686', '-', '3', '1', 'moderntwist旗舰店','320594000201512000000','%s','%s'," \
    #          "'天猫卖家首页信息加载完毕！', 'TM','YTXD20180829100518TMYTXD0000001');"%(int(time.time()),123123,time.strftime('%Y-%m-%d %H:%M:%S'),time.strftime('%Y-%m-%d %H:%M:%S'))
    # print (insert_sql)
    # mysql.insert_data(insert_sql)



