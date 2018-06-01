#-*-coding:utf-8-*-
'''
Created on 2018年5月29日

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
    #  remove BOM  #utf-8编码下会有BOM标志符表示该编码方式，占据3字节
        if config_data[:3] == codecs.BOM_UTF8:
            config_data = config_data[3:]
            files = codecs.open(config_path,'w')#可以指定一种编码模式打开，不会出现编码的问题
            files.write(config_data)#把去掉BOM的文件重新写入并保存退出
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
如果config.ini文件中还有其他的setions,get和set的方法如上  
'''     

# if __name__=="__main__":
#     readconfig = ReadConfig()
#     print readconfig.get_https('scheme')
            
     