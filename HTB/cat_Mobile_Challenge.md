on downloading and unraring we see an ab file: `cat.ab`

Run the following command to extract the backup file
```bash
( printf "\x1f\x8b\x08\x00\x00\x00\x00\x00" ; tail -c +25 backup.ab ) | tar xfvz -
```

the extracted files will show an image, on the document of the image at the bottom is the flag :)
