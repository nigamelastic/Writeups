for i in {1..1040}   # you can also use 
do  
    echo $i
    curl http://167.71.130.31:31259/flag >> flag.txt 
done

