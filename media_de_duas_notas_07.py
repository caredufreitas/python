'''entre no programa duas notas de um aluno calcule e mostre a média'''
print('{:-^40}'.format('MÉDIA DO ALUNO'))
n1 = float(input('Entre com a primeira nota: '))
n2 = float(input('Entre com a segunda nota: '))
media = (n1 + n2) / 2
print('Com {} na primeria nota e {} na segunda a média é {:.1f} '.format(n1, n2, media))
print('{:-^40}'.format('FIM'))

