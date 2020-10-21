from cipher import AESCipher
import sys
import getpass

password = getpass.getpass('password> ')
password2 = getpass.getpass('confirm> ')
if password != password2:
    print('Passwords do not match.')
    sys.exit(0)

# 暗号化
aes_cipher = AESCipher(password)
encryptText_byte = aes_cipher.encrypt('this is a pen')
encryptText_str = encryptText_byte.decode()
with open('e', 'w', encoding='utf-8') as f:
    f.write(encryptText_str)

# #復号
# plainText = aes_cipher.decrypt(encryptText)
# print(plainText)