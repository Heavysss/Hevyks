# Игра отгадай цифру от 1 до 10
from random import randint  # Сделал как професионал.Респект.

print('''
Игра отгадай цифру от 1 до 10
Правила:

1. У тебя 3 попытки
2. Не пиши символы(мне просто впадло делать ответку в коде)
3. Пиши целочисленые выражения
''')

life = 3
random = randint(1, 10)


while True:              # Нужно правильно расставить операторы if elif else. Наверное не нужно, уже начинается бред.
    if life != 0:
         numb = int(input('Введите число от 1 до 10 '))
    if life == 0:
        print('Ты проиграл')
        break
    elif numb == random:
        print('Поздравляю, вы выиграли')
        break
    else:
        if numb < random:
            print('Больше')
        else:
            print('Меньше')
        life -= 1
        print('У тебя осталось ' + str(life) + ' жизни')

# Дааа, игра слишком лёгкая в плане кодинга(если я правильно использую это слово) возможно в следующий раз что-нибудь добавлю ещё
# Игра сделана из интереса и из-за того что делать было нехер 02.10.2019 0:03
