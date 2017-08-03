#! /bin/bash
www=$2
txt=$3
/usr/bin/python  /opt/zabbix/share/zabbix/alertscripts/weixin.py  123  "$www"  "$txt"
