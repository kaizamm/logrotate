#!/bin/bash
to_mail=$1
subject=$2
body=$3
mailxFile=~/mailx.tmp
#echo "$body">$mailxFile
#dos2unix -k $mailxFile
# cat ~/mailx.txt| /bin/mailx -s "$subject" "$to_mail"
echo "$body"|tr -d \\r |/bin/mailx   -s "$subject" "$to_mail" 
