# Урок 6
# Срез списка [List slicing & indexing]
# Срез списка работает как с функцией range()
list = [0,1,2,3,4,5,6,7,8,9,10]

list2 = list[2:4]   # Это работает как от индекса 2 включительно до индекса 4 не включительно
# Итогом будет список от 2 до 3

print(list2)

# Так же можно индекс среза пропустить тоесть
list2 = list[::]    # Это можно понять как срезать от начала до конца

print(list2)    # Получится просто такой же список

# Можно указать ещё и шаг индексированого среза
list2 = list[::2]
'''Это понимается как от начала списка тоесть от 0 он считает(0 включительно)
0,1 это считается как шаг 2 тоесть начало всегда считается как 1 следующее число как 2
и получается что программа выдает 0,2,4,6,8,10  
Очень глупо но можно сказать он пропускает 1 число так как он считает 1 число
с которого началось как часть шага'''
print(list2)

# В срезах можно использовать отрицательное значение в 3 аргументе

list2 = list[::-2]
print(list2)

list2 = list[-3:0:-1]    # Можно сделать и так, получается от -3 индекса а это 8 до начала и шаг с конца
print(list2)

list2 = list[-3:]
print(list2)

list2 = list[::-1][:5]    # Можно поставить ещё один оператор индексирования и делать с индексами что хочешь
print(list2)

list2 = list[-1]    # Получается даже когда аргумент отрицательный то всёравно 0 будет считатся как индекс
print(list2)

