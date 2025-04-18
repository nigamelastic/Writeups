from os import urandom
from Crypto.Cipher import AES
#from secret import MESSAGE
MESSAGE=r'HTB{ASDASDASDASD}'
assert all([x.isupper() or x in '{_} ' for x in MESSAGE])


class Cipher:

    def __init__(self):
        self.salt = urandom(15)
        print(self.salt)
        print("------------")

        key = urandom(16)
        print(key)
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, message):
        return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


def main():
    cipher = Cipher()
    encrypted = cipher.encrypt(MESSAGE)
    encrypted = "\n".join([c.hex() for c in encrypted])

    with open("output1.txt", 'w+') as f:
        f.write(encrypted)


if __name__ == "__main__":
    main()
