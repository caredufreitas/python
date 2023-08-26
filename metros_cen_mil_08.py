'''entre no programa com um valor em metros saia com ele em centimetros
milimetros'''
print('{:-^40}'.format('CONVERSOR DE MEDIDA'))
medida = float(input('Digite a \033[1;32m(MEDIDA)\033[m para converter: '))
print('\033[1;34m{}\033[m Mtr.'.format(medida))
# conversão kilometro, hectometro, decametro
print('Kilômetro = \033[1;34m{}\033[mkil.'.format(medida / 10 ** 3))
print('Hectômetro = \033[1;34m{}\033[mhec.'.format(medida / 10 ** 2))
print('Decâmetro = \033[1;34m{}\033[mdec.'.format(medida / 10 ** 1))
# conversão decimetro, centimetro, milimetro
print('Decímetro = \033[1;34m{:.0f}\033[mdec.'.format(medida * 10))
print('Centímetro = \033[1;34m{:.0f}\033[mcen.'.format(medida * 100))
print('Milímetro = \033[1;34m{:.0f}\033[mmil.'.format(medida * 1000))
print('{:-^40}'.format('FIM'))
