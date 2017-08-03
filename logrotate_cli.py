#!/usr/bin/env python
# _*_ coding: UTF-8 _*_
#BGP-NETAM-01
__author__ = "kaiz"

import sys,os,requests,time,re
cur_time = time.strftime('%Y-%m-%d-%H:%M',time.localtime(time.time()))

if __name__ == "__main__":
  session = requests.Session()
  session.post('http://172.30.33.183:7991/login', json={
    'username': 'Lkaiz',
    'password': 'kaiz@123',
    'eauth': 'pam',
  })
  try:
    hostname = sys.argv[1]
    log_path = sys.argv[2]
    bak_path_ = sys.argv[3]
    save_days = sys.argv[4]
    resp = session.post('http://172.30.33.183:7991', json=[{
      'client': 'local',
      'tgt': hostname,
      'fun': 'state.sls',
      'arg': ['logrotate'],
      'kwarg': {"pillar":{"log_path":log_path,"bak_path_":bak_path_,"save_days":save_days}},
    }])
    a = str(resp.json())
    print "INFO:" + a
    m = re.search("The function \"state.sls\" is running as PID",a)
    if m is not None:
      #若能匹配到The function \"state.sls\" is running as PID这个，则取出jid
      list = a.strip().split()
      index = list.index("jid")+1
      jid = re.search("\d+",list[index])
      jid = jid.group()
      #取出jid后执行类似salt '*' saltutil.signal_job 20140211102239075243 15
      resp = session.post('http://172.30.33.183:7991', json=[{
      'client': 'local',
      'tgt': hostname,
      'fun': 'saltutil.signal_job',
      'arg': [ jid,'15'],
    }])
      aa = resp.json 
      with open("/tmp/logrotate.log","w") as f:
        f.write(cur_time+':'+str(aa)+"\n")
      print "INFO:"+"saltutil.signal_job jid 15"+str(aa)
  except Exception, e:
    err = str(e)
    err = "EROR"+":"+cur_time+":"+err 
    print err
    with open("/tmp/logrotate_err.log","w") as f:
      f.write(err)
