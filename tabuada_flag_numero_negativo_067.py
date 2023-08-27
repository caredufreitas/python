'''entre no programa um número inteiro e mostre sua tabuada e condição de parada
um valor negativo'''
print('{:-^40}'.format('TABUADA'))
while True:
	num = int(input('Quer ver a tabuada de que número ou -1 para sair? '))
	if num < 0:
		break
	for i in range(1, 11):
		print(f'\033[1;34m{num} x {i:2} = {num * i}\033[m')
print('{:-^40}'.format('FIM'))
