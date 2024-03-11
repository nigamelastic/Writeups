from pwn import *
import time
HOST = "83.136.252.32"
PORT = 45669

io = remote(HOST, PORT)

data = io.recvuntil(b"Are you ready? (y/n)").decode()
print(data)
io.sendline(b"y")

data = io.recvuntil(b"Ok then! Let's go!").decode()
print(data)
temp=''
while True:
    
    scenario=io.recv().decode()
    print(scenario)
    #temp = temp+io.recv().decode()
    #scenario = io.recvuntil(b"What do you do?").decode()

    scenario=scenario.replace('What do you do?','')
    scenario=scenario.replace(',','-')
    scenario = scenario.replace(' ','')
    scenario = scenario.replace('GORGE','STOP')
    scenario = scenario.replace('PHREAK','DROP')
    scenario = scenario.replace('FIRE','ROLL')
    scenario = scenario.replace('\n','')
    print('_____________________')
    print(scenario)
    response=scenario
    io.sendline(response.encode())
    
io.close()
print("Game over!")

