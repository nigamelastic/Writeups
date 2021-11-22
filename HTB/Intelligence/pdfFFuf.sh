#!/usr/bin/env bash
d=2020-01-01
while [ "$d" != 2022-12-31 ]; do 
  e=$d-upload.pdf 
  echo $e >> dateoutput.txt
  d=$(date -I -d "$d + 1 day")
  #ffuf -d "FUZZ" --input-cmd '$e' -u http://intelligence.htb/documents/FUZZ
done
