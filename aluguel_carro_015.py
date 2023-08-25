'''escreva um programa que pergunte a quantidade de KM percorridos por um carro
alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preco a pagar, sabendo
que o carro custa R$60 por dia e R$0.15 por KM rodado'''
print('{:-^40}'.format('ALUGUEL DE CARROS'))
km_percorrido = float(input('Quatidade de \033[1;34mKM\033[m percorridos pelo carro: '))
dias_alugado = int(input('Quantidade de \033[1;34mdias\033[m pelo quais foi alugado: '))
preco = (dias_alugado * 60) + (km_percorrido * 0.15) # regra do negócio 
print(f'O total a pagar \033[1;34mR${preco:.2f}\033[m pelo carro alugado. ')
print('{:-^40}'.format('FIM'))
