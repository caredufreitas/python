'''entre no sistema com um valor em Reais saia com quantos Dolar 
pode comprar com este valor'''
 # 5.44  valor na data 29/06/20
reais = float(input('Digite o valor em R$'))
dolar = reais / 5.44
print(f'Com \033[1;34mR${reais:.2f}\033[m você pode comprar \033[1;34mU${dolar:.2f}\033[m Americanos. ')
