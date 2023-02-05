#!/usr/bin/env bash

## Creating the Directory Structure
mkdir $1
mkdir -p $1/nmap
mkdir -p $1/DirectoryBF
mkdir -p $1/SubdomainEnum
mkdir -p $1/Exploits

## Copying the Template
sed -e s/10.11.1./$2/g CTF_template.ctd > $1/Writeup.ctd
 




