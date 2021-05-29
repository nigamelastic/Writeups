#!/usr/bin/env bash

#sample usage
echo "USAGE:  ./portScan.sh <inputip> <outputfile>"
echo ""

if [ $# -ne 2 ]; then
    echo "the script requires exactly 2 arguments please check the usage"
	echo ""
 	exit 
fi

#for displaying the number of arguments suplied
#echo "$#"




ports=$(nmap -p- --min-rate=1000 -T4 10.10.10.27 | grep ^[0-9] | cut -d '/' -f1 | tr '\n' ',' | sed s/,$//)

nmap -PN -sC -sV -p$ports $1 -oN $2  
