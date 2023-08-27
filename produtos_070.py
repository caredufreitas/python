'''entre no programa o preço de vários produtos mostre uma mensagem se quer continuar a cadastrar
e final mostre:
a)qual é o total gasto na compra
b)quantos produtos custam mais de 1000
c)qua é o nome do produto mais barato'''
prod_nome = ' '
total = acima_100 = cont = menor = 0
print('{:-^40}'.format('CADASTRO E ANÁLISE DE PRODUTO'))
while True:
	cont += 1 # icrementando ao contador 
	print(f'-- {cont}ª Produto --')
	nome = str(input('Entre com nome do produto: ')).strip().capitalize()
	preco = float(input('Entre com preço do produto R$'))
	total += preco  # total da compra
	if preco > 1000:  # preco acima de 1000
		acima_100 += 1
	if cont == 1:  # menor produto
		menor = preco
		prod_nome = nome
	else:
		if preco < menor:
			menor = preco
			prod_nome = nome
	op = ' '
	while op not in 'SN':
		op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
	if op in 'N':
		break
print(f'O total gasto na compra foi R$\033[1;32m{total:.2f}\033[m. ')
print(f'R$\033[1;32m{acima_100}\033[m produto custa acima de R$\033[1;32mR$1000\033[m. ')
print(f'O produto R$\033[1;32m{prod_nome}\033[m é o mais barato, custa R$\033[1;32mR${menor}\033[m.')
print('{:-^40}'.format('FIM'))
