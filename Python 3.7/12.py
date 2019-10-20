test = [0,1,2,3,4,[5,6,7],8,9,10]

print(test[6])

test1 = 'Hey'

print(test1[2])

test2 = [0,1,2,3,4]

test2 *= 2

print(test2)

test3 = ['Саня','Коля','Женя']

if 'Саня' in test3:
    print('Саня на связи')
if 'Влад' not in test3:
    print('Не, такого у нас нет')

test4 = []

test4.append("Hey")
test4.append(2+2)
test4.append([1,2,3,4])

print(test4)

print(test3[0][0])

test5 = [5,6,1,2,3,4,5,6,7]

print('В переменной test5 находится ' + str(len(test5)) +' обьектов')

test6 = [0,1,2,[3,4,5,6,7,8,9,10,11,12]]

print('В переменной test6 находится ' + str(len(test6)) +' обьектов')


test7 = ['Alex','Braser','Relis']
test7.remove('Braser')

print(test7)
print('В списке находится ' + str(len(test7)) +' обьектов')

test8 = [0,1,2,4]
test8.insert(3,3)
test8.insert(0,-1)
print(test8)



