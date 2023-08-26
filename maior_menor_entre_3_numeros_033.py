'''entre com três números pelo usuário e mostre qual é o maior e o menor'''
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
maior = n1
if n2 > maior:
	maior = n2
if n3 > maior:
	maior = n3
menor = n1
if n2 < menor:
	menor = n2
if n3 < menor:
	menor = n3
print(f'O maior número é \033[1;34m{maior}\033[m, e o menor número é \033[1;34m{menor}\033[m')
