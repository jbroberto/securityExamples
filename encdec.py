from Crypto.Cipher import AES
import hashlib

key = '123456789'
h = hashlib.md5()
h.update(key.encode())
key = h.hexdigest()
# comprimento multiplo de 16 bytes
msg = "Mensagem txtplan"
cipher_suite = AES.new(key.encode())

print("Texto a ser cifrado: ", msg)
enc = cipher_suite.encrypt(msg)
print("Texto cifrado: ", enc)
print("Texto decifrado: ", cipher_suite.decrypt(enc).decode('utf-8'))
