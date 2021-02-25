import requests




baseURL=r'http://167.71.246.232:8080/rabbit_hole.php?page='
randomString=r'cE4g5bWZtYCuovEgYSO1'

result=requests.get(baseURL+randomString)
x=result.text



for i in range(100):
    result =requests.get(baseURL+x.splitlines()[1].strip())
    x=result.text
    print (x)

    with open("response.txt", "a") as myfile:
        myfile.write(x.splitlines()[0].strip()+","+x.splitlines()[1].strip()+"\n")