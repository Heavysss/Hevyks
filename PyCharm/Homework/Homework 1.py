# Программа для вычисление идеального веса
# Ver 0.1
print(''
      'Здравствуйте это программа вычисления идеального веса\n'
      'В программе приведенны некоторые формулы:\n'
      '1. Формула Брока\n'
      '2. Мечта Лоренца(для женщин)\n')

while True:
    i = int(input('Введите какую формулу хотите выбрать: '))
    if i == 0:
        break
    elif i == 1:
        def Formula_broka(height):
            y = (height - 110.0)* 1.15
            return y

        x = float(input('Введите свой рост: '))
        Brok = Formula_broka(x)
        print('Ваш идеальный вес: ' +str(Brok))
    elif i == 2:
        def Lorencz(height):
            y = (height - 100) - (height - 150)/2
            return y
        x = float(input('Введите свой рост: '))
        print('Ваш идеальный вес:',Lorencz(x))



