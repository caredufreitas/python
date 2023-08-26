'''entre no programa o nome completo de uma pessoa e mostre.
a)O nome com todas as letras maiúsculas
b)O nome com todas as letras minúsculas
c)Quantas letras tem ao todo (sem considerar os espaços)
d)Quantas letras tem o primeiro nome'''
print('{:-^40}'.format('ANALISADOR DE STRING'))
nome = str(input('Digite seu nome completo: '))
print(f'\033[1;34m{nome}\033[m')
print(f'Em maiúsculo → \033[1;34m{nome.upper()}\033[m')
print(f'Em minúsculo → \033[1;34m{nome.lower()}\033[m')
dividido = nome.split()
agrupado = ''.join(dividido)
print(f'Possui \033[1;34m{len(agrupado)}\033[m letras. ')
print(f'Primeiro nome \033[1;34m{dividido[0]}\033[m, contém \033[1;34m{len(dividido[0])}\033[m letras. ')
print('{:-^40}'.format('FIM'))
