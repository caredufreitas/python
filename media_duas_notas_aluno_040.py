'''entre com duas notas de um aluno calcule a media e mostre no final de acordo com a média
abaixo de 5.0 reprovado, entre 5.0 e 6.9 recuperacao, 7.0 ou superior aprovado'''
nota_01 = float(input('Digite a nota 01: '))
nota_02 = float(input('Digite a nota 02: '))
media = (nota_01 + nota_02 ) / 2
print(f'Com a média \033[1;34m{media:.1f}\033[m seu status é, ', end='')  #\033[m cor, :.1f com 1 casa depois da vírgula
if media < 5.0:
	print('\033[1;31mReprovado.\033[m ')
elif 5.0 >= media <= 6.9:
	print('\033[1;33mRecuperação.\033[m ')
else:
	print('\033[1;34mAprovado.\033[m ')
print('{:-^40}'.format('FIM'))
