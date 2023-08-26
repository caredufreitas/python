'''entre no programa com um valor qualquer e saia com 
o seu dobro, triplo, raiz quadrada'''

from math import sqrt
print('{:-^40}'.format('DOBRO | TRIPLO | RAIZQ'))
valor = int(input('Digite um valor: '))
print('{} seu Dobro {} '.format(valor, valor * 2))
print('{} seu Triplo {} '.format(valor, valor * 3))
print('{} sua Raiz Quadrada (Fórmula matemática valor ** (1/2)) é {:.2f} '.format(valor, valor ** (1 / 2)))
print('{} sua Raiz Quadrada (Módulo sqrt()) {:.2f} '.format(valor, sqrt(valor)))
print('{:-^40}'.format('FIM'))

