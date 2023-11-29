the white rabbit

--> fromzsteg--> this made no sense
b1,bgr,lsb,xy       .. text: "9!AmUEcn"
b1,rgba,lsb,xy      .. text: "q]39QW{[YW"
b2,g,lsb,xy         .. text: "AEAUAQEUAUDDDP@"
b2,rgb,msb,xy       .. text: "\"( (*(*(\"("
b3,r,lsb,xy         .. file: gfxboot compiled html help file
b3,rgb,lsb,xy       .. file: gfxboot compiled html help file
b3,rgb,msb,xy       .. file: Apple DiskCopy 4.2 image H\200 A\222 \011\202, 8388617 bytes, 0x92200882 tag size, 0x90 encoding, 0x0 format                                           
b4,r,lsb,xy         .. file: PDP-11 UNIX/RT ldp
b4,rgb,lsb,xy       .. file: Targa image data (257-4368) 

________________________________________________________

so i used `https://stylesuxx.github.io/steganography/`
and found the following: 

`"You need time : RxabLA7UQ9k 

bnnjm://jumnyvch.wig/y49gG4xD"`

replace b with h so every 5th alphabet idk what this cypher is called its not rot5

https://patebin.com/e49mMGdJ

this didnt work so i used [caeser shift](https://www.dcode.fr/shift-cipher)  and got this


`https://pastebin.com/e49mM4dJ`

which has this in the pastebin

`gssor://vvv.xntstad.bnl/vzsbg?u= `


caser shifting it again give the following
`'https://www.youtube.com/watch?v` and adding it with our initial we get `https://www.youtube.com/watch?v=RxabLA7UQ9k`

the ctf creater said i need to check the comments on the video and i found this

You need time challenge : 68747470733a2f2f616e6f6e66696c65732e636f6d2f5a66753656344c356f632f74696d655f776176

on converting from hex to ascii i get
`https://anonfiles.com/Zfu6V4L5oc/time_wav` which as per the creator was the flag although the link was dead