'''escreva um programa que leia vários números inteiro saia com a quantidade de números 
digitados e a soma entre eles condicão de parada 999'''
flag = cont = total = 0
print('{:-^40}'.format('SOMA DO VALORES DIGITADOS'))
while flag != 999:
	flag = int(input('Digite um número ou 999 para sair: '))
	if flag != 999:
		cont += 1
		total += flag
print(f'Foram \033[1;32m{cont}\033[m números digitados. ')
print(f'E \033[1;32m{total}\033[m é a soma entre eles. ')
print('{:-^40}'.format('FIM'))
