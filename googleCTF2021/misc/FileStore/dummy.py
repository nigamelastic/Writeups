import secrets, string

'''i=["jeher",2,3,4,5]
for x,y in i:
	print(x)
	print(y)'''


fid = "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(16))
print(fid)
