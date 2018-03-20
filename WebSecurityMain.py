#encoding:utf-8
import optparse
import json
import os
import sys
import InfoGet
from module_import import *




def initoptparse():
    parser=optparse.OptionParser()
    group1=optparse.OptionGroup(parser,"This is use for collect the information")
    group1.add_option('--info',dest="IGmode",type="string",help='''there have some mode to get IP information:
                                                                    --info IPinfo-IP getplace xx.xx.xx.xx    this is use to get IP location''',metavar="infoGetmode")
    parser.add_option_group(group1)
    group2=optparse.OptionGroup(parser,"This have some WebAttack Mode")
    group2.add_option('--WH',dest="WHmode",type="string",help='''Web HTTP Attack mode,mode have:
                                                                                                --WH HeaderAttack-Host HostPayload Hostargv''')
    parser.add_option_group(group2)
    options, args = parser.parse_args()
    return options,args

if __name__ == "__main__":
    options,args=initoptparse()
    if options.IGmode:
        modeT=options.IGmode
        runmoduleI("InfoGet.{0}".format(str(options.IGmode).replace('-','_._')),args[0],args[1:])
    elif options.WHmode:
        modeT=options.WHmode
        runmoduleW("WebAttack.HTTP_correlation.{0}".format(str(options.WHmode).replace('-',"._")),args[0],args[1:])
        print args
    else:
        pass 
    