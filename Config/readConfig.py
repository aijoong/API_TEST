#-*-coding:utf-8-*-
'''
Created on 2018��5��29��

@author: zhouqianru
'''
import os
import codecs
import configparser

base_path = os.path.split(os.path.realpath(__file__))[0]
config_path = os.path.join(base_path,'config.ini')


class ReadConfig:
    def __init__(self):
        fd = open(config_path)
        config_data = fd.read()
    #  remove BOM  #utf-8�����»���BOM��־����ʾ�ñ��뷽ʽ��ռ��3�ֽ�
        if config_data[:3] == codecs.BOM_UTF8:
            config_data = config_data[3:]
            files = codecs.open(config_path,'w')#����ָ��һ�ֱ���ģʽ�򿪣�������ֱ��������
            files.write(config_data)#��ȥ��BOM���ļ�����д�벢�����˳�
            files.close()
            
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)
    
    
    def get_https(self,name):
        value=self.cf.get("HTTPS",name)
        return value
    
    def set_https(self,name,value):
        self.cf.set("HTTPS",name,value)
        with open(config_path,'w+') as f:
            self.cf.write(f)        
'''
���config.ini�ļ��л���������setions,get��set�ķ�������  
'''     

# if __name__=="__main__":
#     readconfig = ReadConfig()
#     print readconfig.get_https('scheme')
            
     