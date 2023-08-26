'''entre no programa com o valor da casa, salário do comprador, em quantos anos ele vai pagar o empréstimo
processe o valor da prestação mensal sabendo que ele não pode exeder 30% do salário 
ou então o emprestimo será negado'''
print('{:-^40}'.format('EMPRÉSTIMO BANCÁRIO'))
casa = float(input('Entre com o valor da casa R$'))
salario = float(input('Digite o valor do salário R$'))
prestacao = int(input('Digite quantidade anos vai pagar: '))
prestacao_mensal = casa / (prestacao * 12)  # valor da casa / 12 meses de 1 ano * quatidade de ano a pagar
porcentagem_salario = (salario * 30 / 100)
print(f'Com o preço da casa de R$\033[1;34m{casa:.2f}\033[m, e teu salário de R$\033[1;34m{salario:.2f}\033[m. ')
print(f'\033[1;31m30%\033[m do teu salário é equivalente há R$\033[1;34m{porcentagem_salario:.2f}\033[m. ')
print(f'O valor da prestação da casa é de R$\033[1;34m{prestacao_mensal:.2f}\033[m em \033[1;31m{prestacao}\033[m parcelas. ')
print('\033[1;34mEmpréstimo Aprovado.\033[m ' if prestacao_mensal <= porcentagem_salario else '\033[1;31mEmpréstimo Negado.\033[m ')
print('{:-^40}'.format('FIM'))
