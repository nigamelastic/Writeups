#!/usr/bin/env bash


if [ $# -eq 3 ]; then
    ffuf -w $2:FUZZ -u $1/FUZZ -recursion -recursion-depth 2 -of csv -o $3.csv

elif [ $# -eq 4 ]; then
    ffuf -u $1/FUZZDIR.FUZZEXT -w $3:FUZZEXT,$2:FUZZDIR -of csv -o $4.csv 
else
#sample usage
echo "USAGE:  $0 <url> <wordlistfile> <[optionsl]extensionfile> <outputfile> "
fi

#for displaying the number of arguments suplied
#echo "$#"


