'''entre com um numero e saia com uma mensagem de este numero é primo'''
print('{:-^40}'.format('NÚMERO PRIMO'))
num = int(input('Digite um número: '))
total = 0
for i in range(1, num + 1):  # i=1, num acima de 1, num + 1 contagem até o valor exato
	if num % i == 0:
		print('\033[1;33m', end=' ')
		total += 1  # somar o total de divisoes
	else:
		print('\033[1;31m', end=' ')
	print(f'{i}', end=', ' if i < num else ' ')
print(f'\033[m\nO número \033[1;33m{num}\033[m foi divísivel \033[1;33m{total}\033[m. vezes')
print('POR ISTO ELE É PRIMO' if total == 2 else 'POR ISTO ELE NÃO É PRIMO')
print('{:-^40}'.format('Fim'))
