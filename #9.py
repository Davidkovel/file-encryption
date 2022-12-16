import pyAesCrypt

password = input('Введите пароль для шифривания файла: ')

# encrypt
pyAesCrypt.encryptFile('резюме.txt', 'резюме.txt.aes', password)

# decrypt
pyAesCrypt.decryptFile('резюме.txt.aes', 'резюмеout.txt', password)
