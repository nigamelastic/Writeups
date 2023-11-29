from os import urandom
from Crypto.Cipher import AES
MESSAGE='HTB{JJJJJJJJJJJJJJJJJJJJJJJJ}'


class Cipher:
    
    def __init__(self):
        self.salt =  b'\x41' * 15
        key =  b'\x42' * 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, message):
        return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


def main():
    cipher = Cipher()
    encrypted = cipher.encrypt(MESSAGE)
    encrypted = "\n".join([c.hex() for c in encrypted])

    with open("output4.txt", 'w+') as f:
        f.write(encrypted)


if __name__ == "__main__":
    main()

