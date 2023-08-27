'''faça um programa que randomize um valor inteiro condicione para um valor par ou impar
entre com um valor do usuário e opnião do usuário perguntando PAR OU IMPAR processe a soma
e se opnião do usuário estiver corretar ele ganha senão perde mostrando o total de tentativas ele
acertou consecutivamente '''
from random import randint
from time import sleep

op_computador = resultado = ' '
total = tentativas = 0
while True:
	print('{:-^40}'.format('JOGO PAR OU IMPAR'))
	computador = randint(0, 10)  # randomiza de 0 à 10
	jogador = int(input('Sua vez entre com um número [0 à 10]: '))
	op_jogador = ' '
	while op_jogador not in 'PI':  # authentica somente P ou I
		op_jogador = str(input('PAR ou IMPAR ')).strip().upper()
	total = computador + jogador
	if total % 2 == 0:
		resultado = 'PAR'
	else:
		resultado = 'IMPAR'

	print('\033[1;34m>>> PROCESSANDO\033[m')
	sleep(1)
	if op_jogador[0] in 'I' and resultado[0] in 'P':  # condicao para perca do jogador
		print(f'Computador = {computador} | Jogador = {jogador} | Total = {total}', end=' → ')
		print(f'\033[1;34m{resultado}\033[m')
		print(f'PERDEU, tente outra vez. ')
		break
	elif op_jogador[0] in 'P' and resultado[0] in 'I':
		print(f'Computador = {computador} | Jogador = {jogador} | Total = {total}', end=' → ')
		print(f'\033[1;34m{resultado}\033[m')
		print(f'PERDEU, tente outra vez. ')
		break
	elif op_jogador[0] in 'P' and resultado[0] in 'P':  # condicao para vitoria do jogador
		print(f'Computador = {computador} | Jogador = {jogador} | Total = {total}', end=' → ')
		print(f'\033[1;34m{resultado}\033[m')
		print(f'VENCEU, Você é BOM. ')
		tentativas += 1
	elif op_jogador[0] in 'I' and resultado[0] in 'I':
		print(f'Computador = {computador} | Jogador = {jogador} | Total = {total}', end='')
		print(f'\033[1;34m{resultado}\033[m')
		print(f'VENCEU, Você é BOM. ')
		tentativas += 1
print(f'Você venceu \033[1;34m{tentativas}\033[m vezes. ')
print('{:-^40}'.format('FIM'))
