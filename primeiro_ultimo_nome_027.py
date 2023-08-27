'''entre no programa com o nome completo de um pessoa saia com 
seu primeiro nome e último nome'''
print('{:-^40}'.format('FIRST NAME | LAST NAME'))
nome = str(input('Digite seu nome completo? ')).strip().split()
print(f'Seu primeiro nome {nome[0]}')
print(f'Seu último nome {nome[-1]}')
print('{:-^40}'.format('FIM'))
