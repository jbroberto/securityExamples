from Crypto.Cipher import AES

# comprimento deve ser multiplo de 16 bytes
key = '1234567890123456'
# comprimento deve ser multiplo de 16 bytes
msg = "Mensagem txtplan"
cipher_suite = AES.new(key.encode())

print("Texto a ser cifrado: ", msg)
enc = cipher_suite.encrypt(msg)
print("Texto cifrado: ", enc)
print("Texto decifrado: ", cipher_suite.decrypt(enc).decode('utf-8'))
