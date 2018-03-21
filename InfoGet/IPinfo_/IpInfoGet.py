#encoding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import json
import re

def GetIpPlace(IPdata):
    url="https://sp0.baidu.com/8aQDcjqpAAV3otqbppnN2DJv/api.php?query={0}&co=&resource_id=6006&t=1521545961313&ie=utf8&oe=gbk&cb=op_aladdin_callback&format=json&tn=baidu".format(IPdata)
    s=requests.get(url).text
    return json.loads(re.findall(r'op_aladdin_callback\((.*)\)',s)[0])['data'][0]['location']

if __name__ == "__main__":
    print GetIpPlace("2.2.2.2") 