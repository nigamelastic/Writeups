#!/usr/bin/env bash
echo "USAGE: $0 <inputip>"
echo ""

if [ $# -ne 1 ]; then
    echo "the script requires exactly 1 arguments please check the usage"
        echo ""
        exit 
fi

## Creating the Directory Structure
mkdir $1
mkdir -p $1/nmap
mkdir -p $1/DirectoryBF
mkdir -p $1/SubdomainEnum
mkdir -p $1/Exploits

## Copying the Template
sed -e s/10.11.1./$1/g CTF_template.ctd > $1/Writeup.ctd
 




