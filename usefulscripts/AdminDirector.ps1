

# Create a directory where only administrators have full control
# Replace 'SecureFolder' with the name of your desired folder
mkdir SecureFolder

# Reset permissions to default for the folder
icacls SecureFolder /reset /t /c

# Disable inheritance and remove inherited permissions
icacls SecureFolder /inheritance:d /t /c

# Grant full control to Administrators and SYSTEM
icacls SecureFolder /grant "Administrators:(OI)(CI)F" /t /c
icacls SecureFolder /grant "SYSTEM:(OI)(CI)F" /t /c

# Deny access to all other users, including authenticated users
icacls SecureFolder /deny "*S-1-5-11:(OI)(CI)(DE,DC,WDAC,WO,WD,AD,WEA,WA)" /t /c
