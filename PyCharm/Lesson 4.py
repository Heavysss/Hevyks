# Урок 4
# Новые типы данных None и Dictionary

None  # Это тип данных, обозначающий пустоту


# Вообще в ранних своих программах я уже сталкивался с None, когда писал функции, и не понимал почему это появляется
# None появляется в следствии того что в функцию ничего не возвращается тоесть.

def void():
    print('That void')


print(void())  # В этом запросе мы проосим вывести результат функции void и показать возвращаемое значение
void()  # Если бы я ввёл так то я бы просто получил тот код который поместил в функцию

# Словарь - Dictionary

foo = {  # Создание словаря производится фигурными скобками
    'ключ1': 'значение1',  # Вообще можно сказать что словарь это неизменяемый список
    'ключ2': 'значение2',
    # Словари очень удобные в том что ты обращаешься к ключу что-бы получить значение а не к индексу
    'ключ3': 'значение3',
    'ключ4': 'значение4'
}

print(foo['ключ1'],
      foo['ключ2'])  # Вызов значения происходит так - "имя словаря['ключ']"
# В случаем если запросить ключ которого нет в словаре вобросится исключение KeyError
# Словарь в словаре допустим
# Словарь принимает ключ только от простых типов данных int,str,float

# Можно сделать словарь работников с номерами телефонов
# contacts = {
#     'Алексей Чижурин':'+3806343232',
#     'Валерий Берин':'+38099232312'
# }
# find = input('Имя работника: ')
# if find in contacts:
#     print('Работник найден ' + contacts[find])
# else:
#     print('Работник не найден')

# Метод get возвращает второй внесенный аргумент если ключ не был найден
contacts = {
    'Алексей Чижурин':'+3806343232',
    'Валерий Берин':'+38099232312'
}

print(contacts.get('Алекс Сандер','Такого работника нет'))  # Вместо того что-бы выбросить исключение он нам отвечает(возвращает) вторым внесенным параметром(аргументом)
# Если бы второй параметр не был внесен то выдало тип данных None тоесть пустота(По-этому ключу пустота - если дословно)
# Метод get можно использовать даже как переадресацию

# Урок закончен
