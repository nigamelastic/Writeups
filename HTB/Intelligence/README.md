nmap shows smb
ffuf enumeration shows `http 301` on `documents` directory

In the documents we see `view-source:http://intelligence.htb/documents/2020-01-01-upload.pdf`

on using exiftool we get the following ![output](./2020-01-01-upload.pdf)  with user `Creator: William.Lee`
