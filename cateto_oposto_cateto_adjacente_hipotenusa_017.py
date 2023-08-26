'''entre no sistema com o cumprimento do cateto oposto, cateto adjacente
de um triângulo retângulo qualquer calcule e saia com o valor do
cumprimento da hipotenusa
Matematicamente:
hip = (co ** 2 + ca ** 2) / (1 / 2)
'''
from math import hypot, pow
cores = {'limpa': '\033[m', 'azul': '\033[1;34m'}
print('{:-^40}'.format('CO² | CA² | HIPOTENUSA'))
co = int(input('Digite o cumprimento do Cateto Oposto. '))
ca = int(input('Digite o cumprimento do Cateto Adjacente. '))
print('{}CO² = {:.2f}\nCA² = {:.2f}\nHipotenusa = {:.2f}{} '
	.format(cores['azul'], pow(co, 2), pow(ca, 2), hypot(co, ca), cores['limpa']))
print('{:-^40}'.format('FIM'))

