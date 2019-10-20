# Тема модули
from name_modul import name_import    # Указывает название модуля и какою функцию конкретно нужно импортировать
import name_modul                     # Имортирует весь модуль
from name_modul import *              # Импортирует всё из модуля(Нужно для того что бы постоянно не указывать название модуля типо random.randint)
from name_modul import name_import, name_import_2, name_import_3     #Можно просто перечислять какие функции нужны
from name_modul import name_import as my_import    # Имя функции можно изменить на стадии импорта

# random это обьект в котором хранятся определенные переменные,функции,методы перед ним нужно ставить точку
from random import randint  # в этом случаем портируется только функция randint
import random  # в этом случае портируется модуль random
from random import * # в этом случае из модуля random портируются все функции и переменные только теперь не нужно добавлять точку
from math import sqrt as coren # В этом случае я переименовал функцию sqrt на то что мне было нужно
from math import sqrt, pi, sin, cos, log # В этом случае я просто взял модуль math и портировал себе его функции которые мне нужны

random.randint()
print(randint(1.10))
