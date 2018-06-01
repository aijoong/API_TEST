#-*-coding:utf-8-*-
'''
Created on 2018��5��29��

@author: zhouqianru
'''

'''
��־���������: ��ʽ���ȼ���֪ͨ�ȵ�
'''
import logging
import threading
from time import ctime
from datetime import datetime
import os

class Log:
    def __init__(self):
    #����һ���ļ���ר�Ű���ʽ���log�ļ� 

        file_path = os.path.abspath(os.path.join(os.getcwd(), ".."))#��ǰ·�����ϲ�·�������ϲ�../..
        log_path = os.path.join(file_path,'Log')
        
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        day_log_path = os.path.join(log_path,str(datetime.now().strftime('%Y-%m-%d_%H-%M-%S')))
        if not os.path.exists(day_log_path):#log����洢�ڶ�Ӧ������ļ���
            os.mkdir(day_log_path)
            
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)
        #����handler
        handler = logging.FileHandler(os.path.join(day_log_path,"output.log"))
        #���� formatter
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
    
    @staticmethod #��������.������ֱ�ӵ���
    
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