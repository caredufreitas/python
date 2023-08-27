'''crie um intervalo de 1 à 500 saia com a soma dos valores que forem impares e 
multiplos de três'''
print('{:-^40}'.format('SOMA IMPARES MULTIPLO DE TRÊS'))
soma = cont = 0
for i in range(1, 500):
	if i % 3 == 0:
		soma += i + 3
		cont += 1
print(f'A soma dos \033[1;32m{cont}\033[m valores impares multiplos de três é \033[1;32m{soma}\033[m')
print('{:-^40}'.format('FIM'))
