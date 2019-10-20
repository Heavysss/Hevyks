#Изичный калькулятор:D

what = input("Какую операцию желаете провести, (+,-)")


a = float(input("Введите первое число: "))

b = float(input("Введите второе число: "))

if what == "+":
    c = a + b
    print("Ответ:" + str(c))    

elif what == "-":
    c = a - b
    print("Ответ:" + str(c))    

else:
    print('Ты что ебобо?')


input(print("Нажми клавишу Enter для того что-бы закончить "))




    
