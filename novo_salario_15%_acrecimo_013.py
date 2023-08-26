'''entre no programa um salário de um funcionário e saia com este
salário com um acrécimo de 15%'''

cores = {'limpa': '\033[m', 'azul': '\033[1;34m'}
print('{:-^40}'.format('ACRECÍMO NO SALÁRIO (%)'))
salario = float(input('Digite o salário do funcionário R$'))
novo_salario = salario + (salario * 15 / 100)
print('O salário de {}R${:.3f}{} passará a ser de {}R${:.3f}{} com 15% de acrécimo. '
	.format(cores['azul'], salario, cores['limpa'],cores['azul'], novo_salario, cores['limpa']))
print('{:-^40}'.format('FIM'))
