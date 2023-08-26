'''entre no programa o ano de nascimento de um atleta e de acorodo com o idade 
mostre até 9 anos Mirim, 14 anos Infantil, 19 anos Junior, 20 anos Sênior, acima Master'''
from datetime import date
ano_atual = date.today().year
print('{:-^40}'.format('CATEGORIA DE UM ATLETA'))
print(f'Ano atual: {ano_atual}')
ano_nascimento  = int(input('Digite o ano de nascimento do Atleta: '))
idade = ano_atual - ano_nascimento
print(f'O atleta tem {idade} anos, está na categoria, ', end='')

if idade <= 9:
	print('\033[1;34mMirim.\033[m ')
elif 9 > idade <= 14:
	print('\033[1;34mInfantil.\033[m ')
elif 14 > idade <= 19:
	print('\033[1;34mJunior.\033[m ')
elif 19 > idade <= 20:
	print('\033[1;34mSênior.\033[m ')
else:
	print('\033[1;34mMaster.\033[m ')
print('{:-^40}'.format('FIM'))
