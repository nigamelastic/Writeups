#!/bin/bash
echo "==========================================================================
		 usage is ./mailer.sh  <your file with emails>  
=============================================================================="
while read mail
	do
 		echo "$mail"
		swaks --from kali --to "$mail" --header  "Subject: http://10.10.14.113" --body "http://10.10.14.113"
	done <  "$1"


