'''crie um programa que leia o primeiro termo e a razao de uma PA na saida mostre os
10 primeiros termos'''
print('{:-^40}'.format('RAZÃO DE UMA PA'))
primeiro = int(input('Digite o PRIMEIRO TERMO: '))
razao = int(input('Digite a RAZÃO: '))
decimo = primeiro + (10 - 1) * razao  # decimo termo de uma PA
for i in range(primeiro, decimo + razao, razao):
	print(i, end=' → ')
print('\n{:-^40}'.format('Fim'))
