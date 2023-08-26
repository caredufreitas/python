'''entre no programa com um número e sai com este número em quantidade
de sequência de fibonacci'''
cont = 3 # a partir do 3 indice começa a lógica
t1 = 0
t2 = 1
print('{:-^40}'.format('SEQUÊNCIA DE FIBONACCI'))
quantidade = int(input('Qual quantidade de números quer ver na Sequência? '))
print(f'\033[1;32m{t1} - {t2} - \033[m', end='')
while cont < quantidade:
	t3 = t1 + t2
	print(f'\033[1;32m{t3} - \033[m', end='')
	t1 = t2
	t2 = t3
	cont += 1
print('FIM')
print('\n{:-^40}'.format('FIM'))
