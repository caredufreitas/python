'''entre com um valor qualquer inteiro e saia com seu sucessor
e antecessor'''

print('{:-^40}'.format('ANTECESSOR | SUCESSOR'))
valor = int(input('Digite um valor: '))
print('{} - Seu sucessor é {}, seu antecessor é {}.'.format(valor, valor + 1, valor - 1))
print('{:-^40}'.format('FIM'))

