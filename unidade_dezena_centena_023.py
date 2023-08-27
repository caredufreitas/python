'''entre no programa com um valor qualquer inteiro / float saía com 
quantidade de unidade, dezena, centena e milhar digitados'''
print('{:-^40}'.format('UNIDADE | DEZENA | CENTENA | MILHAR'))
num = int(input('Digite um números até (\033[1;34m9999\033[m): '))
print(f'Número digitado:\033[1;34m{num}\033[m ')
print(f'''Contém.
Unidades = \033[1;34m{num // 1 % 10}\033[m
Dezena = \033[1;34m{num // 10 % 10}\033[m
Centena = \033[1;34m{num // 100 % 10}\033[m
Milhar = \033[1;34m{num // 1000 % 10}\033[m''')
print('{:-^40}'.format('FIM'))
