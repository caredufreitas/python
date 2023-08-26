'''crie uma tupla de nome e preço de produtos e saia com ele em forma
tabular nome e respectivos preços'''
print('-' * 46)
print('{:^46}'.format('LISTAGEM DE PREÇOS'))
print('-' * 46)
lista = ('Caderno', 8.90, 'Lápis', 0.30, 'Borracha', 0.70, 'Apontador', 0.40, 'Cola Branca', 2.90, 
	     'Corretivo', 1.90, 'Giz de cera', 1.80, 'Tesoura', 4.90, 'Caneta', 0.60)
for pos in range(0, len(lista)):
	if pos % 2 == 0:
		print(f'{lista[pos]:.<39}', end='')
	else:
		print(f'R$ {lista[pos]:>3.2f}')
print('-' * 46)
