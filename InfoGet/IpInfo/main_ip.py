#encoding:utf-8

import os
import json
import exceptions
import re
import IpInfoGet

class Main_IP(object):
    def __init__(self,ipdata):
        self.ipdata=ipdata
    
    def AnalysisIP(self):
        IP_re=re.findall(r'([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})\.([\d]{1,3})',self.ipdata)
        if IP_re:
            if len(IP_re[0])!=4:
                raise TypeError("IP data type error,you should enter like this :192.168.0.1")
            else:
                for _ in IP_re[0]:
                    if int(_)<0 or int(_)>255:
                        raise ValueError("{0}-->{1} should in 0-255".format(self.ipdata,_))
        else:
            raise TypeError("IP data type error,you should enter like this :192.168.0.1")     
    
    def runAll(self):
        self.AnalysisIP()

if __name__ == "__main__":
    Main_IP("546.564.54.585").runAll()