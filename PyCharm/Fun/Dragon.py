import random
import time

def displayintro():
    print('''Вы искатель приключений.
    Вы нашли заброшеный город ну или точнее что осталось от города,
    на земле лежат обожённые листы бумаги и там вы смогли разгрядеть дракона
    и в какую пещеру нужно пойти что-бы найти его сокровища''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Вы обнаружили две пещеры в какую пойдете(нажмите кдавишу 1 или 2)')
        cave = input()
    return cave

def checkCave(choosenCave):
    print('Вы приближаетесь к пещере...')
    time.sleep(2)
    print('С пещеры идёт очень холодный воздух')
    time.sleep(4)
    print('Дракон восстает перед вами и смотрит на вас убийстеным взгядом и...')
    time.sleep(5)

    friendlyCave = random.randint(1,2)

    if choosenCave == str(friendlyCave):
        print('...дает вам забрать сокровища и шанс уйти')
    else:
        print('...не оставляет вам и шанс на сопротивление моментально испепеляя вас')

playAgain = 'да'
while playAgain == 'да' or playAgain == 'Да':
    displayintro()
    caveNumber = chooseCave()
    checkCave(caveNumber)
    time.sleep(2)
    print('Попытаете удачу ещё раз? ( да или нет)')
    playAgain = input()
