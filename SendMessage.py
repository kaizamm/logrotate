#!/usr/bin/python
# -*- encoding:utf-8 -*-

# -----------------------------------------
# Purpose:
#     Call SMS platform interface to send zabbix alarm message
# ------------------------------------------
# @Author : weiye
# @Date : 2016-06-16
# @Complete basic functions
# -----------------------------------------

import sys
import json
import urllib
import httplib

besType = "007"
deptType = "005"
thirdType = "bcloud-monitoring"

HttpTimeout = 3

ApiInterServer = "172.16.4.55"
ApiInterPort = 8080
ApiInterURL = "/sms-frontal/MessageController/sendMsg"

def SendMessage(phoneNumber,content,deptType,besType,thirdType):
    httpClient = None
    try:
        params = urllib.urlencode({"phoneNumber":phoneNumber,"content":content,"deptType":deptType,"besType":besType,"thirdType":thirdType})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
        httpClient = httplib.HTTPConnection(ApiInterServer,ApiInterPort,timeout=HttpTimeout)
        httpClient.request('POST', ApiInterURL,params,headers)
        response = httpClient.getresponse()
        print response.status , response.read()
    except Exception,e:
        print ("Error Info : %s"%e)
    finally:
        if httpClient:
            httpClient.close()

if __name__ == "__main__":

    phoneNumber = sys.argv[1]
    subject = sys.argv[2]
    text = sys.argv[3]
    context = subject + "\n" + text
    SendMessage(phoneNumber,context,deptType,besType,thirdType)

