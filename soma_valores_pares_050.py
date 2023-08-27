'''crie um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem
pares se o valor digitado for impar desconsidere-os'''
print('{:-^40}'.format('SOMA DE VALORES PARES'))
soma = cont = 0
for i in range(0, 6): # i somente a interação
	print(i + 1, end='')
	num = int(input(' - Digite um número: '))
	if num % 2 == 0:
		soma += num
		cont += 1
print(f'A soma de \033[1;33m{cont}\033[m lidos no total de números pares é \033[1;33m{soma}\033[m')
print('{:-^40}'.format('FIM'))
