#-*- coding: UTF-8 -*-
import logging
import logging.config
import Config.var_config as conf

# 读取日志配置文件
logging.config.fileConfig(conf.parent_dir_path + "\\config\\logger.conf")
# 选择一个日志格式
logger = logging.getLogger("example02")#或者example01

def debug(message):
    # 定义dubug级别日志打印方法
    logger.debug(message)

def info(message):
    # 定义info级别日志打印方法
    logger.info(message)

def warning(message):
    # 定义warning级别日志打印方法
    logger.warning(message)
