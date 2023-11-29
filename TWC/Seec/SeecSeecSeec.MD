Downloaded the jpg, went through all the tools in my arsenals without password, didnt find anything so tried with the password of the song written over it without the `,`

ie `SickSickSick` using steghide using the following command `steghide extract -sf SeeC_SeeC_SeeC.jpg` did that and i got a huge string in a file.

From the second hint we know that its something to do with if else or xor, so fired up cyberchef (thanks to ava aka nsa bot), and then got this at key 43 that makes a lil sense

`.....begin.see.c.....-*mdadatamdadamtemdatatemdatatamdatemtemda*mdatamdadamtemdatemdamdatamtemdatemt`
apparently that was not correct so i put the entire file on cyberchef, xor with c, then pem to hex , then converted from hex, and then converted that to binary

`https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'UTF8','string':'c'%7D,'Standard',false)PEM_to_Hex()From_Hex('None')From_Binary('None',8)`

this link will do it in the exact order,

the output u get when converted from html:

actually i found that there are more things that can be done in cyberchef:

`https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'UTF8','string':'c'%7D,'Standard',false)PEM_to_Hex()From_Hex('None')From_Binary('None',8)From_HTML_Entity()From_Base64('A-Za-z0-9%2B/%3D',true)PEM_to_Hex()From_Hex('Auto')`


and after even more, few things to remember c is the hint, rot3 cyberchef "c" is the key

`https://gchq.github.io/CyberChef/#recipe=XOR(%7B'option':'UTF8','string':'c'%7D,'Standard',false)PEM_to_Hex()From_Hex('None')From_Binary('None',8)From_HTML_Entity()From_Base64('A-Za-z0-9%2B/%3D',true)PEM_to_Hex()From_Hex('Auto')ROT13(true,true,false,3)Reverse('Character')`

this is the final cybershef code for the key
