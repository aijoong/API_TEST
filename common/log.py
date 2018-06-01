#-*-coding:utf-8-*-
'''
Created on 2018年5月29日

@author: zhouqianru
'''

'''
日志的相关配置: 格式，等级，通知等等
'''
import logging
import threading
from time import ctime
from datetime import datetime
import os

class Log:
    def __init__(self):
    #创建一个文件夹专门按格式存放log文件 

        file_path = os.path.abspath(os.path.join(os.getcwd(), ".."))#当前路径的上层路径，上上层../..
        log_path = os.path.join(file_path,'Log')
        
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        day_log_path = os.path.join(log_path,str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
        if not os.path.exists(day_log_path):#log按天存储在对应的天的文件夹
            os.mkdir(day_log_path)
            
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        #定义handler
        handler = logging.FileHandler(os.path.join(day_log_path,"output.log"))
        #定义 formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s-%(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        
    def get_logger(self):
        return self.logger
    def build_start_line(self,case_no):
        self.logger.info("--------" + case_no + " START--------")
    def build_end_line(self,case_no):
        self.logger.info("--------" + case_no + " END--------")
    def build_case_line(self,case_name,code,msg):
        self.logger.info(case_name+" - Code:"+code+" - msg:"+msg)

class MyLog:
    log = None
    mutex = threading.Lock()
    
    def _init_(self):
        pass
    
    @staticmethod #可以类名.方法名直接调用
    
    def get_log():
        
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log=Log()
            MyLog.mutex.release()
            
        return MyLog.log
if __name__ == "__main__":
    log = MyLog.get_log()
    logger = log.get_logger()
    logger.debug("test debug")
    log.build_start_line("123")
    logger.info("test info")
    log.build_end_line("123")