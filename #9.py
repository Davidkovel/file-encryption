import pyAesCrypt

password = input('Введите пароль для шифривания файла: ')

# encrypt
pyAesCrypt.encryptFile('резюме.txt', 'резюме.txt.aes', password)

# decrypt
pyAesCrypt.decryptFile('резюме.txt.aes', 'резюмеout.txt', password)

# lst = [19, 5, 42, 2, 77]
#
# a = min(lst)
# lst1 = []
#
# for i in lst:
#     if a != i:
#         lst1.append(i)
# b = min(lst1)
# res = a + b
# print(res)
#     low = 0
#     high = len(list)-1
#
#     while low <= high:
#         mid = (low + high)
#         guess = list[mid]
#         if guess == item:
#             return mid
#         if guess > item:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
# print(binarn_search([4,2,1,3,9, 6, 4], 4))
# def reverse_string(s):
#     chars = list(s)
#     for i in range(len(hi) // 2):
#         tems = chars[i]
#         chars[i] = chars[len(hi) - i -1]
#         chars[len(hi) - i - 1] = tems
#
#     return ''.join(chars)
#
# print(hi)
# print(reverse_string(hi))