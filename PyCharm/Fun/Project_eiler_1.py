# Задача 1
# Числа, кратные 3 или 5 до 1000
b = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        b = b + i
print(b)

