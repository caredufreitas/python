'''entrada de dados do teclado string, int, float'''
nome = str(input('Qual é seu nome? '))
idade = int(input('Qual sua idade? '))
peso = float(input('Qual é seu peso [kg]? '))
print('Processando... ')
print('Olá {} você tem {} anos de idade e pesa {} kilos. '.format(nome, idade, peso))

