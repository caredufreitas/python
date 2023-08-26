'''entre com ano de nascimento de uma pessoa processe a idade e de acordo com o resultado mostre
se ele ainda vai se alistar no serviço militar, se é tempo de se alistar, se já passou do tempo de se alistar,
saia também com o tempo que falta ou passou do prazo'''
from datetime import date
ano_atual = date.today().year  # randomiza a data do sistema e pega somente o ano
print('{:-^40}'.format('ANÁLISE DE ALISTAMENTO MÍLITAR'))
print(f'Ano Atual: \033[1;31;40m{ano_atual}\033[m')
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento  # calcula a data atual com ano de nascimento saber idade
print(f'Você tem \033[1;34m{idade}\033[m anos. ')
if idade < 18:
	print(f'Ainda vai se alistar no serviço Militar falta \033[1;34m{18 - idade}\033[m ano. ')
elif idade == 18:
	print(f'Hora de se alistar no seriviço Militar com \033[1;34m{idade}\033[m anos. ')
else:
	print(f'Passou do tempo de alistamento Militar com \033[1;34m{idade - 18}\033[m anos a mais. ')
print('{:-^40}'.format('FIM'))
