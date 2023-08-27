'''randomize um valor inteiro entre (0, 5) entre com o valor do usuário
e mostre se o valor randomizado for igual ao do usuário, VENCEU, ou PREDEU'''

from random import randint
from time import sleep
computador = randint(0, 5)
print('{:-^40}'.format('JOGO DA ADIVINHAÇÃO'))
usuario = int(input('Digite um número de [0, 5]: '))
sleep(1)
print(f'Computador → {computador} ←   |   Usuário → {usuario} ←')
print('\033[1;32mVocê Venceu...\033[m' if computador == usuario else '\033[1;31mVocê Perdeu...\033[m')
print('{:-^40}'.format('FIM'))
