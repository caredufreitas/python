'''entre no sistema com o preço de um produto e saia com um novo
preco com 5% de desconto'''

print('{:-^40}'.format('DESCONTO NO PRODUTO (%)'))
preco = float(input('Digite o preço do produto R$'))
novo_preco = preco - (preco * 5 / 100)
print('O produto que custava R${:.3f} com 5% de desconto custará R${:.3f} '.format(preco, novo_preco))
print('{:-^40}'.format('FIM'))
