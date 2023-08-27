'''entre no programa com o número que o usuário quer ver a tabuada
e saia com seu produto'''
print('{:-^40}'.format('TABUADA'))
num = int(input('Quer ver a Tabuada de que Número: '))
for i in range(1, 11):
	print(f'\033[1;34m{num} X {i} = {num * i}\033[m')
print('{:-^40}'.format('FIM'))
