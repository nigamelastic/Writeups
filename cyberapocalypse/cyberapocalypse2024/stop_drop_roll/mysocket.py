import socket
import time
HOST = "83.136.252.32"
PORT = 45669

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
sock.connect((HOST, PORT))

# Receive initial data
data = sock.recv(4096).decode()
print(data)

# Send the response
sock.sendall(b"y\n")

# Receive more data
#data = sock.recv(4096).decode()
#print(data)
scenario_chunk=''
while True:
    # Receive data until a newline character is encountered
    scenario_chunk = scenario_chunk+sock.recv(4096).decode()
    time.sleep(.25)
    # Print the received data
    print("Received:", scenario_chunk)

    # Check if the received chunk contains the prompt "What do you do?"
    if "What do you do?" in scenario_chunk:
        # If found, extract the scenario and process it
        scenario = scenario_chunk
        scenario=scenario.replace(f"What do you do?","")
        scenario=scenario.replace(f"Ok then! Let's go!","")
        scenario=scenario.replace(',','-')
        scenario = scenario.replace(' ','')
        scenario = scenario.replace('GORGE','STOP')
        scenario = scenario.replace('PHREAK','DROP')
        scenario = scenario.replace('FIRE','ROLL')
        scenario = scenario.replace('\n','')
        print('_____________________')
        print(scenario)
        sock.sendall(scenario.encode()+b"\n")
        scenario_chunk=''
# Close the socket connection
sock.close()
print("Game over!")

