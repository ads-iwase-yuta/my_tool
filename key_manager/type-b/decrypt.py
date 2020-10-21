from cipher import AESCipher
import sys
import getpass

password = getpass.getpass('password> ')

#復号
aes_cipher = AESCipher(password)
with open('e', 'r') as f:
    encryptText_str = f.read()
    encryptText_byte = encryptText_str.encode()
    try:
        plainText = aes_cipher.decrypt(encryptText_byte)
    except:
        print('[ERROR] decrypt failed. please check PW.')
        sys.exit(1)
    print(plainText)