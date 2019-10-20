# fun
# while True:
#    x = int(input('Сколько вам лет: '))
#    if x == 0:
#        break
#    elif x <= 10:
#        print('Jun')
#    elif x <= 30:
#        print('freelance')
#    elif x <= 50:
#        print('senior')
#    elif x <= 80:
#        print('hardsenior')
#    else:
#        print('No life hardsenior')

# Psyholigic test

result = 0
print('''Вы:
1. Учусь
2. Работаю
''')

answer = int(input(': '))

if answer == 1:
    answer += 1
else:
    answer += 2
print('''Когда нечего делать чем вы себя занимаете:
1. Смотрю в потолок
2. Смотрю на небо
3. Ищу фильм который хотел посмотреть когда-то
4. Читаю
''')

answer1 = int(input(': '))

if answer1 == 1:
    answer += 1

elif answer1 == 2:
    answer += 4

elif answer1 == 3:
    answer +=2

else:
    answer += 3

if answer > 5:
    print('Почти равен Кодзим... богу')
else:
    print('Дебил не образованый')
