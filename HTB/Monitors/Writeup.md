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

