from random import randint
from time import sleep
import emoji
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
lista = list()
game = list()
print(f'{Fore.BLACK}''*=' * 10)
print(f'   {Fore.RED + Style.BRIGHT}Mega Lottery   ')
print(f'{Fore.BLACK}''*=' * 10)
ask = int(input(f'{Fore.YELLOW}Games: '))
total = 1
while total <= ask:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    game.append(lista[:])
    lista.clear()
    total += 1
print('\n')
print(f'{Fore.RED}''*=' * 3, f'{Style.BRIGHT + Back.MAGENTA} Sorting {ask} games', f'{Fore.RED}''*=' * 3)
print('\n')
for index, listagem in enumerate(game):
    print(f'{Fore.BLUE}Lottery {index + 1}: {Fore.CYAN + Style.BRIGHT}{listagem}')
    sleep(1)
print(emoji.emojize(f'{Fore.GREEN}:four_leaf_clover::four_leaf_clover::four_leaf_clover::four_leaf_clover::four_leaf_clover::four_leaf_clover: Good Lucky!! :four_leaf_clover::four_leaf_clover::four_leaf_clover::four_leaf_clover::four_leaf_clover::four_leaf_clover:'))
