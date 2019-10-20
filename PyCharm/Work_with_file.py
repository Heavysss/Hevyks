# Урок 3.1
# Программа для копирования файлов от HowdyHo

# filename1 = input('Введите название какой файл нужно скопировать: ')
# filename2 = input('Введите название нового файла: ')

# file1 = open(filename1, 'r')
# file2 = open(filename2, 'w')

# file2.write(file1.read())
# print('Копирование успешно завершено')

# file1.close()
# file2.close()

# Программа для бэкапа файла

# filename1 = input('Введите название какой файл нужно скопировать: ')
# filename2 = 'Backup_' + filename1
#
# file1 = open(filename1, 'rb')        # К любому из режимов работы можно приставить режим b - binary mode
# file2 = open(filename2, 'wb')        # Что в свою очередь позволяет уже работать с бинарными файлами типо любой медиа файл, аудио,фото, видео и т.д
#
# file2.write(file1.read())
# print('Создание копии файла завершено')
#
# file1.close()
# file2.close()

# Программа для считывания строк

# file = open('Heavys.txt', 'r')
#
# strings = file.readlines()      # readlines дословно чтение линий
# for i in strings:
#     print(i)
#
# file.close()

# with open('Heavys.txt', 'r') as f:  # with это специальная конструкция с её помощью можно сделать временную переменную
#     print(f.read())                 #и в рамках этой конструкции с отступом сделать что нужно с файлом и по завершению всех строк под with файл автоматически закроется







