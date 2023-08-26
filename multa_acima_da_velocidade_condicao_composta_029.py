'''entre no programa a velocidade de um carro em KM/h condicao
o carro ultrapassar 80 KM/h saia com um mensagem que ele foi multado
a multa vai custar R$7.0 por cada KM/h acima do limite'''
print('{:-^40}'.format('SISTEMA DE MULTA'))
velocidade = float(input('Em qual velocidade (KM/h) está o carro? '))
mensagem = '\033[1;31mMULTADO...\033[m' if velocidade > 80.0 else '\033[1;34DENTRO DOS LIMITES.\033[m'
print(f'{mensagem}')
if 'MULTADO' in mensagem:
	multa = (velocidade - 80) * 7.0
	print(f'Valor da Multa R$\033[1;31m{multa:.2f}\033[m')
print('{:-^40}'.format('FIM'))
