'''entre com a idade e sexo de várias pessoas condicao a cada pessoa o sistema mostra uma mensagem
para que queira cadastra mais e no final mostre:
a) quantas pessoas tem mais de 18 anos
b) quantos homens foram cadastrados
c) quantas mulheres tem menos de 20 anos'''
maior_18 = cad_homen = cad_mulher = cont = 0
while True:
	cont += 1
	print(f'-- {cont}ª Pessoa --')
	idade = int(input('Entre com sua idade: '))
	sexo = ' '
	while sexo not in 'MF':  # authentica o sexo M/F
		sexo = str(input('Entre com seu sexo [M/F]: ')).strip().upper()[0]
	if idade > 18:  # idade maior 18
		maior_18 += 1
	if sexo in 'M':  # qtd de mulheres
		cad_homen += 1
	if sexo in 'F' and idade < 20: # qtd de mulheres acima de 20 anos
		cad_mulher += 1
	op = ' '
	while op not in 'SN':  # authentica o cadastro S/N
		op = str(input('Quer cadastrar mais pessoas [S/N]: ')).strip().upper()[0]
	if op in 'N':
		break
print('{:^40}'.format('ANÁLISE'))
print(f'Total de \033[1;34m{maior_18}\033[m pessoas maiores de 18 anos. ')
print(f'Total de \033[1;34m{cad_homen}\033[m homens cadastrados. ')
print(f'Total de \033[1;34m{cad_mulher}\033[m mulheres com menos de 20 anos. ')
print('{:-^40}'.format('FIM'))
