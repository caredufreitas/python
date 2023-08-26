'''randomize um valor interio de 0 à 10 entre com um valor do jogador
para adivinhar até acertar mostrando no final quantos palpites foram necessários'''
from random import randint
computador = randint(0, 10)
print('{:-^40}'.format('JOGO ADVINHAÇÂO'))
acerto = palpites = 0
while acerto == 0:
	jogador = int(input('Sua vez digite um número [0, 10]: '))
	if computador == jogador:
		acerto += 1
	else:
		print(f'\033[1;31mNão é este\033[m')
		if jogador > computador:
			print(f'Meu valor é menor. ')
		else:
			print(f'Meu valor é maior. ')
		palpites += 1
print(f'COMPUTADOR - \033[1;33m{computador}\033[m | JOGADOR - \033[1;33m{jogador}\033[m')
print(f'Voçê acertou com \033[1;33m{palpites}\033[m palpites. ')
print('{:-^40}'.format('FIM'))
