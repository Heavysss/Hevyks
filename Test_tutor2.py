from random import randint
x = 0
quit = ('выйти','закончить','завешить','отступить','покинуть палубу','уйти в небытье')
while True:
	y = input()
	y.lower()
	x = randint(1,2)
	if y in quit:
		break
	elif x == 1:
		print('Да')
	else:
		print('Нет')