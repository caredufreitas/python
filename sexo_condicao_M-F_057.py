'''entre no programa com o sexo de uma pessoa más continue se o sexo for M ou F'''
print('{:-^40}'.format('CREDENCIAL DE ENTRADA'))
sexo = ' '
while sexo not in 'MF':
	sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
	if sexo not in 'MF':
		print(f'\033[1;31mErro! tente novamente. \033[m')
print('Logado no sistema. ')
print('{:-^40}'.format('FIM'))
