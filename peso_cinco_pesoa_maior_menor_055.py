'''escreva um programa que leia o peso de cinco pessoas e no final mostre qual 
o maior e qual o menor peso lido'''
maior = menor = 0
for i in range(0, 5):
	peso = float(input('Digite seu peso (Kg.): '))
	if i == 0:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso
print(f'O maior peso lido foi \033[1;33m{maior}\033[mKg. ')
print(f'O menor peso lido foi \033[1;33m{menor}\033[mKg. ')
print('{:-^40}'.format('FIM'))
