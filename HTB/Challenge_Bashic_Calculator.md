
Looking at the challenge source code we could see that there are restricted symbols `string{" ", "`", "$", "&", "|", ";", ">"}`

Also the challenge uses `bash -c` with operands added with something like this `(3+4)`

 which will display the final calculated code like this
 ```
"echo $((" + op + "))"
```
so if we replace the operand inputs with this

```
{cat,/flag.txt})#( 
```

it will run `cat /flag.txt` and show us the output



