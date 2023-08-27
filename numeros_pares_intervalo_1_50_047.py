'''crie um intervalo de 1 à 50 e saia com  todos os seus números pares'''
print('{:-^40}'.format('NÚMEROS PARES EM UM INTERVALO'))
for i in range(1, 51, 2):
	print(i, end=' → ' if i < 49 else ' ')
	# print(i)
print('\n{:-^40}'.format('FIM'))
