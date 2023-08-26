'''entre no programa com uma string e 
a) mostre quantas vezes apareçe o caracter A
b) em que posição ela aparece primeria vez
c) em que posição ela aparece a última vez'''
print('{:-^40}'.format('CONTAGEM DE CARACTERE'))
frase = str(input('Digite uma frase qualquer? ')).strip()
print('O caractere \033[1;34m\'A\'\033[m aparece \033[1;34m{}\033[m vezes '.format(frase.count('A')))
print('A primeria posição \033[1;34m{}\033[m, ele apareçe. '.format(frase.find('A') + 1))  # colocar saida para usuário inicio 1
print('A última posição \033[1;34m{}\033[m, ele apareçe. '.format(frase.rfind('A') + 1)) # varre da direita para esquerda
print('{:-^40}'.format('FIM'))
