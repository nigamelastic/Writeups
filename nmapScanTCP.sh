#!/usr/bin/env bash

#sample usage
echo "USAGE: $0 <inputip> <outputfile>"
echo ""

if [ $# -ne 2 ]; then
    echo "the script requires exactly 2 arguments please check the usage"
        echo ""
        exit 
fi

#for displaying the number of arguments suplied
#echo "$#"




#ports=$(nmap -p- --min-rate=1000 -T4 $1 | grep ^[0-9] | cut -d '/' -f1 | tr '\n' ',' | sed s/,$//)

ports=$(nmap -sT -p0-65535 --min-rate=1000 -T4 $1 | grep ^[0-9] | cut -d '/' -f1 | tr '\n' ',' | sed s/,$//)

#ports=$(nmap -sU -sT -p0-65535 --min-rate=1000 -T4 -iL $1 | grep ^[0-9] | cut -d '/' -f1 | tr '\n' ',' | sed s/,$//)
echo "the ports found are: $ports"


# use -PN if nmap probes do not detect a host
#  nmap -PN -sC -sV -p$ports $1 -oN $2  
echo $2
nmap -A -v -p$ports $1 -oA $2 
#_____________________ to run from a file_____________________________
#nmap -A -v -p$ports -iL $1 -oN $2

#nmap -A -sS -v -p$ports $1 -oN $2 
