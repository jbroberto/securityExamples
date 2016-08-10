from Crypto.Cipher import AES
import hashlib


def pad(s):
    return s + ((16-len(s) % 16) * '*')


# chave nao multiplo de 16 bytes
key = '123456789'
# cria-se um objeto hash do tipo MD5
h = hashlib.md5()
# a chave e passada para este objeto
h.update(key.encode())
# a chave passa a ser o hash MD5 da chave original
key = h.hexdigest()
# comprimento nao multiplo de 16 bytes
msg = "Nova mensagem txtplan"
# uso de pad() para tornar a msg multiplo de 16 bytes
msgpad = pad(msg)
cipher_suite = AES.new(key.encode())

print("Texto a ser cifrado: ", msg)
enc = cipher_suite.encrypt(msgpad)
print("Texto cifrado: ", enc)
dec = cipher_suite.decrypt(enc).decode('utf-8')
dec = dec.strip('*')
print("Texto decifrado: ", dec)