'''entre no programa o número do primeiro termo, razao e mostre sua progressão aritmética
interagindo com usuário quantos termos a mais ele deseja que o sistema o sistema encerra
quando ele desejar mostrar 0 termos mostre'''
cont = 0
total = 10  # ATRIBUI OS 10 PRIMEIROS TERMOS
print('{:-^40}'.format('RAZÃO DE UMA PROGRESSÃO ARITMÉTICA'))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao: '))
while True:
	while cont < total:
		print(f'\033[1;33m{primeiro}\033[m', end=' - ')
		primeiro += razao  # ATRIBUI A RAZAO NO TERMO
		cont +=1
		print('PAUSA')
	mais = int(input('\nQuer ver mais termos ou 0 para encerrar? '))
	total += mais  # ATRIBUI O VALOR A MAIS NO TOTAL
	if mais == 0:  # CONDIÇÃO DE PARADA 0
		break
print('{:-^40}'.format('FIM'))
