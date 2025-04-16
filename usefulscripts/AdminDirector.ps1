# Simple script that removes default inheritance and denies writing / modifying contents by regular (authenticated) users. Only Administrators / SYSTEM can ("Built-In\Users" is S-1-5-32-545 + "NT-AUTHORITY\Authenticated Users" is S-1-5-11). 
# the script was created to install vbox in a different directory
# replace vbox with the name of your folder
mkdir vbox
icacls vbox /reset /t /c
icacls vbox /inheritance:d /t /c
icacls vbox /grant *S-1-5-32-545:(OI)(CI)(RX)
icacls vbox /deny  *S-1-5-32-545:(DE,WD,AD,WEA,WA)
icacls vbox /grant *S-1-5-11:(OI)(CI)(RX)
icacls vbox /deny  *S-1-5-11:(DE,WD,AD,WEA,WA)
