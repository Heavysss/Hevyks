# Программа которая читает текст из буфера обмена

import pyperclip

print('Убедитесь что вы скопировали текст в буфер обмена')
print('Нажмите Enter для продолжения программы')
input()
print('-----------------------------')


s = pyperclip.paste()
b = s
s = s.replace('\n','')
s = s.replace('\r','')
s = s.replace(',','')
s = s.replace('.','')
s = s.replace('!','')
s = s.replace('?','')
s = s.replace('"','')
s = s.replace('-','')
str1 = len(s)
str2 = len(b)

print('Количество символов без знаков препинания, переносов строк и пробелов: {}'.format(str1))
print('Количество символов со всеми знаками и переносами строк: {}'.format(str2))