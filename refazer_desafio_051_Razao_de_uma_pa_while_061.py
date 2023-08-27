'''entre no programa o primeiro termo e a razão de uma PA processe os 10 primeiros termos
'''
print('{:-^40}'.format('PROGRESSÃO ARITMÉTICA'))
primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
# decimo = primeiro + (10 - 1) * razao
cont = 0
while cont < 10:
	print(f'\033[1;32m{primeiro}\033[m', end='')
	primeiro += razao
	cont += 1
print('\n{:-^40}'.format('Fim'))
