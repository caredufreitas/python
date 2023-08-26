'''entre no programa o nome de uma cidade e saia mostrando 
a informação que ela começa com SANTO'''
print('{:-^40}'.format('COMEÇA COM SANTO'))
nome_cidade = str(input('Digite o nome de sua cidade: ')).strip().upper().split()
print('SANTO' in nome_cidade[0])
print('{:-^40}'.format('FIM'))

