#!/bin/bash
to_mail=$1
subject=$2
body=$3
from_mail='quark\zhihuic'
#from_mail='zhihuic@quarkfinance.com'
smtp="172.16.1.20"
#smtp="172.30.30.32"
passwd="chzhh@1"

/usr/local/bin/sendEmail  -f $from_mail -t $to_mail -s $smtp -u "$subject" -m "$body"  -xu $from_mail -xp $passwd -o message-content-type=text -o message-charset=utf8 -o tls=auto >> /var/log/zabbix/sendEmail.log
