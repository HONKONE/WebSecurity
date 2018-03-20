#encoding:utf-8
import optparse
from InfoGet import *
import json

InfoGet_list=['ipdata','domaindata']

def initoptparse():
    parser=optparse.OptionParser()
    group1=optparse.OptionGroup(parser,"This is use for collect the information")
    group1.add_option('--infoi',dest="ipdata",type="string",help="get the information from ip or the relation information from ip",metavar="IP")
    group1.add_option('--infod',dest="domaindata",type="string",help="get the information from ip or the relation information from domain",metavar="Domain")
    parser.add_option_group(group1)
    options, args = parser.parse_args()
    return options,args

if __name__ == "__main__":
    options,args=initoptparse()
    print options
    for _ in options.keys():
        print _
