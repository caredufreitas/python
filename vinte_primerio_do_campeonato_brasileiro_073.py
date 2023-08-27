'''crie uma tupla com os vinte primeiros colocados do campeonato Brasileiro de Futebol
e mostre:
A) Apenas os 5 primerios colocados
B) Os últimos 4 primeiros colocados
C) Uma lista com os times em ordem alfabética
D) Em que posição da tabela esta o time da Chapecoense'''
vinte_primeiros = ('FLAMENGO', 'SANTOS', 'PALMEIRAS', 'GRÊMIO', 'ATHLETICO-PR',
				   'SÃO PAULO', 'INTERNACIONAL', 'CORINTHIANS', 'FORTALEZA', 'GOIÁS',
				   'BAHIA', 'VASCO', 'ATLÉTICO-MG', 'FLUMINENSE', 'BOTAFOGO',
				   'CEARÁ', 'CRUZEIRO', 'CSA', 'CHAPECOENSE', 'AVAÍ')
print('{:-^40}'.format('ANÁLISE DO CAMPEONATO BRASILEIRO'))
posicao = 0
for pos, i in enumerate(vinte_primeiros):
	if 'CHAPECOENSE' in i:
		posicao += pos
print('-=' * 15)
print(f'Os cinco primeiros times é \033[1;32m{vinte_primeiros[:5]}\033[m')  # slice iguinora o último elemento
print('-=' * 15)
print(f'Os últimos quatro primeiros colocados \033[1;32m{vinte_primeiros[16:]}\033[m')
print('-=' * 15)
print(f'Os times em ordem alfabética \033[1;32m{sorted(vinte_primeiros)}\033[m')
print('-=' * 15)
print(f'A posição que se encontra a \033[1;32mCHAPECOENSE\033[m é a\033[1;32m{posicao}ª\033[m colocação. ')
# print(f'A posição da Chapecoense é {vinte_primeiros.index("CHAPECOENSE") + 1}')
print('-=' * 15)
print('{:-^40}'.format('FIM'))
