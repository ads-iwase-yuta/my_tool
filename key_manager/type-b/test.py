from cipher import AESCipher
import sys
import getpass

# aes_cipher = AESCipher('123456')
# with open('text.txt', 'rb') as f:
#     r = f.read()
#     encryptText_byte = aes_cipher.encrypt(str(r))
#     plainText = aes_cipher.decrypt(encryptText_byte)
#     with open('myfile.txt', 'wb') as ff:
#         ff.write(plainText.encode())
#     # print(type(plainText.encode()))

# aes_cipher = AESCipher('123456')
with open('doc.pdf', 'rb') as f:
    r = f.read()
    print(type(r))
    with open('myfile.pdf', 'wb') as ff:
        one = r.decode()
        two = one.encode()
        ff.write(two)