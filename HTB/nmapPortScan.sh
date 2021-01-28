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


#running masscan on ip txt file supplied and saving it

nmap -PN -sC -sV -p- $1 -oN $2  
