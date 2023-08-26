'''entre no programa a distância de uma viagem em KM saia com o preço da
passagem cobrando R$0.50 por KM para viagens de até 200KM e R$0.45 para viagens mais longas'''

distancia = float(input('Qual a distância da viagem em (KM): '))
preco = distancia * 0.5 if distancia <= 200 else  distancia * 0.45
print(f'Para \033[1;34m{distancia:.2f}\033[mKM o preço da passagem custará R$\033[1;34m{preco:.2f}\033[m.')
