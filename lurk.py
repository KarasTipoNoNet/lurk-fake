import random
from colorama import init, Fore, Style
from tqdm import tqdm
from time import sleep
import os

print('loading files...')

for i in tqdm(range(100), colour = 'green'):
    sleep(random.uniform(0.01, 0.1))

os.system('cls' if os.name == 'nt' else 'clear')

print('loaded! Starting lurk...')

for i in tqdm(range(100), colour = 'green'):
    sleep(random.uniform(0.001, 0.1))

os.system('cls' if os.name == 'nt' else 'clear')

sleep(3)

lang = input('''Select lang:
1. Russian
2. English

Write ONLY NUMBER!
''')

if lang == '1':
    print('Вы выбрали Русский язык!')

    sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')

    sleep(1)

    print('Добро пожаловать в ларк! Это хакерская программа которая собирает айпи адреса и ворует файлы!')

    sleep(3)

    print('идёт загрузка файлов ларка... Пожалуйста подождите...')
    print('Распаковка файлов из: lurkfiles.zip')
    for i in tqdm(range(2134), colour = 'green'):
        sleep(random.uniform(0.001, 0.01))
    print('Распаковка файлов из: backup.zip')
    for i in tqdm(range(873), colour = 'green'):
        sleep(random.uniform(0.001, 0.01))
    print('Распаковка файлов из: lurkplugins.zip')
    for i in tqdm(range(10495), colour = 'green'):
        sleep(random.uniform(0.0001, 0.001))

    print('Загружено! Пожалуйста подождите...')

    sleep(10)

    print('Запуск плагина lurk Ip Collecter...')

    sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')

    print(Fore.GREEN, Style.DIM)
    print('Поиск...')

    while True:
        sleep(random.uniform(3, 10))
        pcipornot = [1, 2]
        pcip = random.choice(pcipornot)
        ip1 = random.uniform(0, 255)
        ip2 = random.uniform(0, 255)
        filenames = ['hentai.mp4', 'melonplayground-v7-1.apk', 'standoff2.obb', 'chromehistory.dll', 'token.txt', 'pornsearch.py']
        filename = random.choice(filenames)

        if pcip == 1:
            print(f'Устройство захвачено! IP: 192.168.{int(ip1)}.{int(ip2)}')
        elif pcip == 2:
            print(f'Устройсво захвачено! IP: 82.145.{int(ip1)}.{int(ip2)}')

        file = open(f'{filename}.txt', 'a')
        file.write('Поскольку ларк шуточный, то тут будет этот текст =)')
        file.close()


elif lang == '2':
    print('You Selected English Language!')

    sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')

    sleep(1)

    print('Welcome to Lurk! This is a hacker program that collects IP addresses and steals files!')

    sleep(3)

    print('Loading lurk files... Please wait...')
    print('Extracting files from: lurkfiles.zip')
    for i in tqdm(range(2134), colour = 'green'):
        sleep(random.uniform(0.001, 0.01))
    print('Extracting files from: backup.zip')
    for i in tqdm(range(873), colour = 'green'):
        sleep(random.uniform(0.001, 0.01))
    print('Extracting files from: lurkplugins.zip')
    for i in tqdm(range(10495), colour = 'green'):
        sleep(random.uniform(0.0001, 0.001))

    print('Loaded! Please wait...')

    sleep(10)

    print('Launching the lurk Ip Collecter Plugin...')

    sleep(3)

    os.system('cls' if os.name == 'nt' else 'clear')

    print(Fore.GREEN, Style.DIM)
    print('Search...')

    while True:
        sleep(random.uniform(3, 10))
        pcipornot = [1, 2]
        pcip = random.choice(pcipornot)
        ip1 = random.uniform(0, 255)
        ip2 = random.uniform(0, 255)
        filenames = ['hentai.mp4', 'melonplayground-v7-1.apk', 'standoff2.obb', 'chromehistory.dll', 'token.txt', 'pornsearch.py']
        filename = random.choice(filenames)

        if pcip == 1:
            print(f'Device captured! IP: 192.168.{int(ip1)}.{int(ip2)}')
        elif pcip == 2:
            print(f'Device captured! IP: 82.145.{int(ip1)}.{int(ip2)}')

        file = open(f'{filename}.txt', 'a')
        file.write('Since the lurk is comic, then this text will be here =)')
        file.close()