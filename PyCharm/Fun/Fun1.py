# Программа отвечающая Да или Нет за принципом рандома
from random import randint
while False:
    i = input()     # Что-бы цикл не двигался сам по себе а через Enter
    x = randint(1,2)
    if x == 1:
        print('Да')
    else:
        print('Нет')
# Подсчёт сколько раз будет Орел сколько Решка
x = 0
y = 0
for i in range(100):
    a = randint(1,2)
    if a == 1:
        x += 1
    else:
        y += 1
print('Решка = ' +str(x) +', Орел = '+str(y))

