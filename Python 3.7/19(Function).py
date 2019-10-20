i = 33

def foo(bar):
    print(bar * 2)
foo(8)
foo(2)
foo(3)
foo(i)

def f(): # Эта функция для вычисление четного числа
    a = 1
    while a == 1:
        print('Введите число')
        x = int(input())
        if x % 2 == 0:
            print('Это четное число')
        else:
            print('Это нечетное число')

def k(): # Эта функция для вычисления большего числа 
    a = 1
    while a == 1:
        x = float(input(''))
        y = float(input(''))
        if x > y:
            print('Это число больше: ' + str(x))
            
        else:
            print('Это число больше: ' + str(y))



            


