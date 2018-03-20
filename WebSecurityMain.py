#encoding:utf-8
import optparse
import json
import os
import sys
import InfoGet
from InfoGet.IpInfo._IP import *
from module_import import *




def initoptparse():
    parser=optparse.OptionParser()
    group1=optparse.OptionGroup(parser,"This is use for collect the information")
    group1.add_option('--infoi',dest="ipdata",type="string",help="get the information from ip or the relation information from ip",metavar="IP")
    group1.add_option('--infod',dest="domaindata",type="string",help="get the information from ip or the relation information from domain",metavar="Domain")
    parser.add_option_group(group1)
    group2=optparse.OptionGroup(parser,"This have some WebAttack Mode")
    group2.add_option('--WH',dest="WHmode",type="string",help='''Web HTTP Attack mode,mode have:
                                                                                                --WH HeaderAttack-Host HostPayload Hostargv''')
    parser.add_option_group(group2)
    options, args = parser.parse_args()
    return options,args

if __name__ == "__main__":
    options,args=initoptparse()
    if options.ipdata:
        Main_IP(options.ipdata).runAll()
    if options.WHmode:
        modeT=options.WHmode
        runmodule("WebAttack.HTTP_correlation.{0}".format(str(options.WHmode).replace('-',"._")),args[0],args[1])
        print args
        
    