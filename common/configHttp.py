#-*-coding:utf-8-*-
'''
Created on 2018Äê5ÔÂ30ÈÕ

@author: zhouqianru
'''

import requests
import Config.readConfig as readconfig
from log import MyLog as Log
import json
from numpy.distutils.conv_template import header
from __builtin__ import None

config = readconfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        global scheme, port, host, timeout
        scheme = config.get_https("scheme")
        host = config.get_https("baseurl")
        port = config.get_https("port")
        timeout = config.get_https("timeout")
        
        self.log = Log.get_log()
        self.logger = self.log.get_logger()
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}
        self.state = 0
    
    def set_url(self,url):
        self.url = scheme + '//' + host +url
        
    def set_headers(self,header):
        self.headers = header
    
    def set_params(self,params):
        self.params = params
    
    def set_data(self,data):
        self.data = data
        
#     def set_files
    def get(self):
        try:
            response = requests.get(self.url, headers = self.headers, params = self.params,timeout = float(timeout))
        except requests.Timeout as err:
            self.logger.error({'message':err.message})
            return None
    def post(self):
        try:
            response = requests.post(self.url, headers = self.headers, data = self.data,timeout = float(timeout))
        except requests.Timeout as err:
            self.logger.error({'message':err.message})
            return None
            










        