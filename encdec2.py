from Crypto.Cipher import AES
import hashlib

# chave nao multiplo de 16 bytes
key = '123456789'
# cria-se um objeto hash do tipo MD5
h = hashlib.md5()
# a chave e passada para este objeto
h.update(key.encode())
# a chave passa a ser o hash MD5 da chave original
key = h.hexdigest()
# comprimento multiplo de 16 bytes
msg = "Mensagem txtplan"
cipher_suite = AES.new(key.encode())

print("Texto a ser cifrado: ", msg)
enc = cipher_suite.encrypt(msg)
print("Texto cifrado: ", enc)
print("Texto decifrado: ", cipher_suite.decrypt(enc).decode('utf-8'))
