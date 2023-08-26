'''randomize e coice pedra, papel, tesoura no programa pergunte ao usuário sua opção
pedra, papel, tesoura com a condição de quem vai ganhar'''
from random import choice
from time import sleep
print('{:-^40}'.format('VAMOS JOGAR'))
sleep(0.5)
print('JO')
sleep(0.5)
print('\033[1;31m{:^5}\033[m'.format('KEN'))
sleep(0.5)
print('PO')
computador = list(['PEDRA', 'PAPEL', 'TESOURA'])  # lista para escolha
escolhido = choice(computador)  # escolhe uma string dentro da lista
jogador = str(input('Escolha [PEDRA, PAPEL, TESOURA]: ')).strip().upper()
print('PROCESSANDO... ')
sleep(1)

if escolhido[:2] == 'PE' and jogador[:2] == 'PE':  # condiçao para o computador 
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='  → ')
	print('\033[1;33mEMPATE\033[m')

elif escolhido[:2] == 'PE' and jogador[:2] == 'TE':
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='  → ')
	print('\033[1;31mPERDEU\033[m')

elif escolhido[:2] == 'TE' and jogador[:2] == 'TE':
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='  → ')
	print('\033[1;33mEMPATE\033[m')

elif escolhido[:2] == 'TE' and jogador[:2] == 'PA':
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='  → ')
	print('\033[1;31mPERDEU\033[m')

elif escolhido[:2] == 'PA' and jogador[:2] == 'PA':
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='  → ')
	print('\033[1;33mEMPATE\033[m')

elif escolhido[:2] == 'PA' and jogador[:2] == 'PE':
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='  → ')
	print('\033[1;31mPERDEU\033[m')

elif jogador[:2] == 'PE' and escolhido[:2] == 'TE':  # condição para o jogador
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='  → ')
	print('\033[1;32mVENCEU\033[m')

elif jogador[:2] == 'TE' and escolhido == 'PA':
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='  → ')
	print('\033[1;32mVENCEU\033[m')

elif jogador[:2] == 'PA' and escolhido == 'PE':
	print(f'Computador - {escolhido} | Jogador - {jogador}', end='')
	print('\033[1;32mVENCEU\033[m')
print('{:-^40}'.format('FIM'))
