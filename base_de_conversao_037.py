'''entre no programa com um valor inteiro, mostre como opção que tipo de valor o usuário que converter
1 binário, 2 octal, 3 hexadecimal'''
print('{:-^40}'.format('CONVERSÂO DE NÚMEROS DE BASE'))
num = int(input('Digite um número: '))
op = int(input('''Entre com a opção:
[1] - Binário
[2] - Octal
[3] - Hexadecimal '''))
print(f'valor digitato {num}', end=' - ')
if op == 1:
	print(f'{bin(num[2:])} - BINÁRIO')  # binário slice 2, tirar o caractere de indentificação 0b
elif op == 2:
	print(f'{oct(num[2:])} - OCTAL')  # octadecimal
elif op == 3:
	print(f'{hex(num[2:])} - HEXADECIMAL')  # hexadecimal
else:
	print(f'{op} INVÁLIDO EXECUTE NOVAMENTE! ')  # inválido para valores inexistêntes
print('{:-^40}'.format('FIM'))
