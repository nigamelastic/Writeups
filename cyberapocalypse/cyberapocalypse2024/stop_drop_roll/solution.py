import * from pwn

pty = process.PTY
p = process(stdin=pty, stdout=pty)

while True:
    data = p.recv()
    if data:
         Process received data
        # ...
        break  # Exit the loop after receiving data
    else:
        # No data received, handle the case (e.g., wait)
        # ...
