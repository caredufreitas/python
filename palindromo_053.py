'''escreva um programa que leia uma frase qualquer e mostre se ela é um palindromo
desconsiderando espaços'''
print('{:-^40}'.format('DETECTOR DE PALINDROMO'))
frase = str(input('Digite uma frase qualquer? ')).upper().strip().split()
frase_agrupada = ''.join(frase)
print(f'{frase_agrupada}  |  {frase_agrupada[::-1]}')
print('PALINDROMO ' if frase_agrupada[:] == frase_agrupada[::-1] else 'NÃO É PALINDROMO ') #[start: stop: step]
print('{:-^40}'.format('FIM'))
