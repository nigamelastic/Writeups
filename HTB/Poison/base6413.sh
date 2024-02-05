data=$(cat input.txt); for i in $(seq 1 13); do data=$(echo $data | sed 's/ //g' | base64 -d); done; echo $data

