'''escreva um programa que leia o nome, idade, sexo de quatro pessoas no final do programa mostre:
A) A média de idade do grupo
B) Qual é o nome do homem mais velho
c) Quantas mulheres têm menos de 20 anos'''
print('{:-^40}'.format('ANÁLISE'))
total = media = cont = mais_velho = tot_mulher = 0
nome_velho = ' '
for i in range(0, 4):
	print('---{}ª {}---'.format(i + 1, 'Pessoa'))
	nome = str(input('Digite teu nome: ')).strip().capitalize()
	sexo = ' '
	while sexo not in 'MF':  # not in 'MF' não acessa
		sexo = str(input('Digite teu sexo: ')).strip().upper()[0]
	idade = int(input('Digite tua idade: '))
	cont += 1
	total += idade
	if cont == 1 and 'M' in sexo:  # condicao para maior idade, atribuicao do nome
		mais_velho = idade
		nome_velho = nome
	else:
		if idade > mais_velho:
			mais_velho = idade
			nome_velho = nome
		
	if 'F' in sexo and idade < 21:
		tot_mulher += 1
media = total / cont  # processa a media
print(f'A média de idade do grupo é \033[1;32m{media:.1f}\033[m anos. ')
print(f'O \033[1;32m{nome_velho}\033[m é o homen mais velho com \033[1;32m{mais_velho}\033[m anos de idade. ')
print(f'Total \033[1;32m{tot_mulher}\033[m mulher com menos de \033[1;32m21\033[m anos de idade. ')
print('{:-^40}'.format('FIM'))
