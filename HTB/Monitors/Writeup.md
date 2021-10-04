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
```

