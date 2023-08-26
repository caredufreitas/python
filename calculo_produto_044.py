'''entre no programa com o preço de um produto considerando o seu preço normal
e condição de pagamento, a vista dinheiro/cheque 10% de desconto, a vista no cartão
5% de desconto, em até 2x no cartão preço normal, em até 3x no cartão 5% de juros'''

preco = float(input('Entre com o preço do produto R$'))
op = int(input('''Condição de pagamento escolha:
[1] - A vista dinheiro/cheque com 10\% de desconto
[2] - A vista no cartão com 5\% de desconto
[3] - Em até 2x no cartão preço normal
[4] - Em até 3x no cartão 5\% de juros\n '''))
condicao = 0
if op == 1:
	print('DINHEIRO/CHEQUE - 10% DE DESCONTO')
	condicao = preco - (preco * 10 / 100)  # 10% desconto
elif op == 2:
	print('CARTÃO - 5% DE DESCONTO')
	condicao = preco - (preco * 10 / 100)  # 5% desconto
elif op == 3:
	print('2x CARTÃO - PRECO NORMAL')
	condicao = preco  # preco normal
elif op == 4:
	print('3x CARTÃO - 5\% de juros')
	condicao = preco + (preco * 5 / 100)  # 5% de juros
else:
	print(f'Operação {op} Inválida. ')
print(f'O produto que custava R${preco:.2f} passará a custar R${condicao:.2f}')
print('{:-^40}'.format('FIM'))
