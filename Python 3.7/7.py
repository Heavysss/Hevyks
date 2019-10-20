pas1 = ('disk33')
pas2 = input('Введите пароль: ')

while pas1 != pas2:
    pas2 = input("Повторите попытку: ")

if pas1 == pas2:
    print('Здравствуйте')
