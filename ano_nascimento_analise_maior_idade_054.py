'''escreva um programa que leia o ano de nascimento de sete pessoas e no final
mostre quantas pessoas ainda não atingiram maior idade e quantas já atingiram '''
from datetime import date
ano_atual = date.today().year
print('{:-^40}'.format('ANÁLISE DE IDADE'))
menor = maior = 0
for i in range(0, 6):
	ano_nascimento = int(input('{}ª Digite o seu ano de nascimento: '.format(i + 1)))
	idade = ano_atual - ano_nascimento
	if idade < 21: # condicao menor 21
		menor += 1
	else:
		maior += 1
print(f'Foram \033[1;32m{menor}\033[m pessoas cadastradas menores de \033[1;33m21\033[m anos. ')
print(f'Foram \033[1;32m{maior}\033[m pessoas cadastradas maiores de \033[1;33m21\033[m anos. ')
print('{:-^40}'.format('FIM'))
