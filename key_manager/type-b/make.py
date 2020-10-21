from cipher import AESCipher
import sys
import getpass

password = getpass.getpass('password> ')
password2 = getpass.getpass('confirm> ')
if password != password2:
    print('Passwords do not match.')
    sys.exit(0)

# 32文字のパスフレーズ(ランダムキー)
pass_phrase = password

aes_cipher = AESCipher(pass_phrase)

# 暗号化
encryptText = aes_cipher.encrypt('plain text')
print(encryptText)

#復号
plainText = aes_cipher.decrypt(encryptText)
print(plainText)