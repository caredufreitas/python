'''entre no programa dois números inteiro e saia com mensagem mostrando a condicao
o primeiro número é maior, o segundo número é maior ou não existe maior e nem menor os dois são
iguais'''
print('{:-^40}'.format('ANÁLISADOR DE NÚMEROS'))
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if  num1 > num2:
	print('\033[1;33mO primeiro número é Maior. \033[m ')
elif num1 == num2:
	print('\033[1;33mNão existe número Maior os dois são iguais.\033[m ')
else:
	print('\033[1;33mO segundo número é Maior.\033[m' )
print('{:-^40}'.format('FIM'))
