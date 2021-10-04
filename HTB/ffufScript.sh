#!/usr/bin/env bash

#sample usage
echo "USAGE:  $0 <url> <wordlistfile> <outputfile>"
echo ""

if [ $# -ne 3 ]; then
    echo "the script requires exactly 3 arguments please check the usage"
        echo ""
        exit
fi

#for displaying the number of arguments suplied
#echo "$#"


ffuf -w $2:FUZZ -u $1/FUZZ -recursion -recursion-depth 2 -of csv -o $3.csv 
