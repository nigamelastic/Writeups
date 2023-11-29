## User

Run nmap and found ftp and ssh

Ran ffuf to find three directories:


* data
* ip
* netstat

check data/0 to download the cap file. open it in wireshare via
 `wireshark 0.cap` go through the file and get the ftp password.

 login to ftp via `ftp 10.10.10.245`
 and get the file via: `GET user.txt`

 use the same password to `ssh` into the linux machine

## Root
 
After you ssh into the linux copy https://github.com/carlospolop/PEASS-ng/tree/master/linPEAS to the linux machine and run it.
in the `capabilities` section of the output , you will see `python3.8` , 
so we can use the following command from  https://gtfobins.github.io/gtfobins/python/#capabilities:

`python3.8 -c 'import os; os.setuid(0); os.system("/bin/bash")'`

and u will have root

