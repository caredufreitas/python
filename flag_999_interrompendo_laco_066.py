'''entre no programa vários números inteiros pelo teclado o programa só vai parar
que o usuário digitar o valor 999 que é condição de parada no final mostre quantos
números foram digitados e qual foi a soma entre eles'''
cont = total = 0
print('{:-^40}'.format('TOTAL DE NÚMEROS DIGITADOS E SOMA'))
while True:
	num = int(input('Digite um número: '))
	if num == 999:
		break
	cont += 1
	total += num
print(f'Foi \033[1;32m{cont}\033[m números digitado e sua soma é de \033[1;32m{total}\033[m. ')
print('{:-^40}'.format('FIM'))
