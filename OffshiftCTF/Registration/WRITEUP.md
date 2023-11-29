# In order to Register u need  a PIN

The site says "The secret pin code for CTF entry is hidden somewhere on this site"

On analayzing all the images i found this link "https://ctfd.offshift.io/files/0617eefb188fec1d9a60e5ec902070ed/CTF3.gif"

after downloading it I ran steghide and stegosuite, they didnt work so finally used https://github.com/evyatarmeged/stegextract  the following repo

by using `sudo ./stegextract CTF3.gif --outfile output.txt`

The output is `secret: 100100100101`


I thought i could convert the binary to ascii or char.

But I just needed to conver binary to decimal

which is "2341"

bam DONE!
