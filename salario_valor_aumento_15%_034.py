'''entre no programa o salário de um funcionário e saia com o seu valor
na condicao para salários superiores a R$1.250 um aumento de 10%, inferiores
aumento de 15%'''
print('{:-^40}'.format('CALCULO DE SALÁRIO'))
sal = float(input('Digite o salário do Funcionário R$'))
if sal < 1250:  # 15%
	novo_sal = sal + (sal * 15 / 100)
else: # 10%
	novo_sal = sal + (sal * 10 / 100)
print(f'Para o salário de R$\033[1;34m{sal:.2f}\033[m seu novo salário é R$\033[1;34m{novo_sal:.2f}\033[m')
print('{:-^40}'.format('FIM'))
