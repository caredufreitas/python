'''entre no programa com a altura e largura de uma parede
em mtr calcule a area e a quantidade de tinta necessária para 
pintá-la considerando que cada litro de tinta pinta 2m²'''

from math import ceil
cores = {'limpa': '\033[m', 'azul': '\033[1;34m'}
print('{:-^40}'.format('CALCULO DE ÁREA'))
largura = float(input('Digite a largura da Parede: '))
altura = float(input('Digite a altura da Parede: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem uma dimensão de \033[1;34m{}\033[m x \033[1;34m{}\033[mmtr. '.format(largura, altura))
print('{}{:.2f}M²{} é sua área de Parede. '.format(cores['azul'], area, cores['limpa']))
print('{}{}-Litros{} de tinta para pintar está área. '.format(cores['azul'], ceil(tinta), cores['limpa']))
print('{:-^40}'.format('FIM'))


