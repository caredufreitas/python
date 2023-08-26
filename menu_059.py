'''crie um programa que leia dois valores e mostre um menu:
[1] - somar, [2] - multiplicar, [3] - maior, [4] - novos números, [5] - sair'''
print('{:-^40}'.format('CALCULADORA'))
flag = 5
cont = maior = menor = 0
while flag == 5:
	num_1 = int(input('Digite o primeiro número: '))
	num_2 = int(input('Digite o segundo número: '))
	op = int(input('''	-- Menu --
	[1] - Somar
	[2] - Multiplicar
	[3] - Maior
	[4] - Novos Números
	[5] - Sair do Programa
	Digite sua opção: '''))
	print('---------------')
	if op == 1:
		print(f'SOMAR')
		print(f'{num_1} + {num_2} = {num_1 + num_2}')
	
	elif op == 2:
		print(f'MULTIPLICAR')
		print(f'{num_1} x {num_2} = {num_1 * num_2}')
	
	elif op == 3:
		print(f'MAIOR')
		if cont == 0:
			maior = num_1
			menor = num_1
		if num_2 > maior:
			maior = num_2
		if num_2 < menor:
			menor = num_2
		print(f'O maior valor é {maior} e o menor valor é {menor} ')
	
	elif op == 4:
		print(f'NOVOS NÚMEROS')
		flag = 5
	
	elif op == 5:
		print(f'SAINDO')
		flag == 0
	
	else:
		print(f'OPERAÇÃO INVALIDA, TENTE NOVAMENTE! ')
print('{:-^40}'.format('FIM'))
