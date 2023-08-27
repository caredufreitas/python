'''randomize valores inteiros de cinco números adicione a tupla mostre a listagem de números
gerados e indique o maior e menor valor na tupla'''
from random import randint
print('{:-^40}'.format('ALEATÓRIO EM TUPLA'))
numeros = (randint(1, 10), randint(1, 10), randint(1, 10),
	 randint(1, 10), randint(1, 10))  # parenteses está dentro de uma tupla
print('Os valores sorteados foram : ', end='')
for n in numeros:
	print(f'\033[1;34m{n}\033[m ',end='')
print(f'\nO maior valor sorteado \033[1;34m{max(numeros)}\033[m')
print(f'O Menor valor sorteado \033[1;34m{min(numeros)}\033[m')
print('{:-^40}'.format('FIM'))
