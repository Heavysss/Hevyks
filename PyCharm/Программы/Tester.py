import pyperclip

input('Убедитесь что в буфере обмена лежит название файла и его тип.'
      'Если всё правильно нажмите Enter'
      '')
filename1 = pyperclip.paste()
filename11 = ('C:\Program Files\JetBrains\PyCharm Community Edition 2019.2.3\Cours Of Python/' +str(filename1) +'.py')
filename2 = ('1'+filename1 +'.txt')
file1 = open(filename11, 'r')
file2 = open(filename2, 'w')

file2.write(file1.read())
print('\nФайл успешно прочитан,перезаписан и закрыт')
file1.close()
file2.close()


