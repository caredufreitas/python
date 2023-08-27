'''entre no programa com um número qualquer e saia
com seu produto em forma de uma tabuada'''
cores = {'limpa': '\033[m', 'azul': '\033[1;34m'}
print('{:-^40}'.format('TABUADA SIMPLES'))
n = int(input('Quer ver a tabuada de que número: '))
print('{}{} x 1 = {}'.format(cores['azul'], n, n * 1))
print('{} x 2 = {}'.format(n, n * 2))
print('{} x 3 = {}'.format(n, n * 3))
print('{} x 4 = {}'.format(n, n * 4))
print('{} x 5 = {}'.format(n, n * 5))
print('{} x 6 = {}'.format(n, n * 6))
print('{} x 7 = {}'.format(n, n * 7))
print('{} x 8 = {}'.format(n, n * 8))
print('{} x 9 = {}'.format(n, n * 9))
print('{} x 10 = {}{}'.format(n, n * 10, cores['limpa']))
print('{:-^40}'.format('FIM'))
