'''leia um ano qualquer e saia com uma mensagem se ele é BISSEXTO'''
# 4 de 4 anos
from datetime import date
print('{:-^40}'.format('ANO BISSEXTO'))
ano = int(input('Digite o ano ou [0] para o ano atual: '))
if ano == 0:
	ano = date.today().year
print(f'O ano, {ano}')
if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0):
	print('\033[1;34mBISSEXTO\033[m.')
else:
	print('\033[1;34mNÃO BISSEXTO\033[m')
print('{:-^40}'.format('FIM'))
