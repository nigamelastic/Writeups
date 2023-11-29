nmap shows smb
ffuf enumeration shows `http 301` on `documents` directory

In the documents we see `view-source:http://intelligence.htb/documents/2020-01-01-upload.pdf`

on using exiftool we get the following ![output](./2020-01-01-upload.pdf)  with user `Creator: William.Lee`

in order to enumerate more pdfs by date I created a ![shellScript](./pdfFFuf.sh) which created a list at ![dateoutput.txt](./dateoutput.txt).

once I got that I used my FFUF script to enumerate it via ` ./ffufScript.sh http://intelligence.htb/documents Intelligence/dateoutput.txt Intelligence/ffufOutputDatePDF.log`

I found a lot of hits which are ![here](./ffufOutputDatePDF.log.csv)

Cleaned it via `cut -d',' -f1 ffufOutputDatePDF.log.csv > PDFFilesFound.txt`

So apart from going through each pdf mind numbingly after downloading and using SMB i finally found a user, though apparently u can use `https://github.com/byt3bl33d3r/CrackMapExec` to enumerate them, I had no clue tbh, I used simple shell command and ran smbclient with password in loop over the users to check. 
PS: `dont be lazy if u are reading this it will cost u more time`

so finally i used the password from `2020-06-04-upload.pdf` 
`smbclient  //intelligence.htb/Users -U 'Tiffany.Molina' `

