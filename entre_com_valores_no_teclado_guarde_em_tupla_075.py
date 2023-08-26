'''leia quatro valor pelo teclado e guarde em uma tupla no final mostre:
A)quantas vezes apareceu o valor 9
B)quantas vezes foi digitado o primeiro valor 3
C) quais foram os numeros pares'''
print('{:-^40}'.format('QUATRO VALORES EM UMA TUPLA'))
num = (int(input('Digite um número: ')),
	   int(input('Digite outro número: ')),
	   int(input('Digite mais um número: ')),
	   int(input('Digite último número: ')))  # parenteses da tupla
print(f'Você digito os valores \033[1;34m{num}\033[m ')
print(f'O valor 9 apareceu \033[1;34m{num.count(9)}\033[m vezes. ')
if 3 in num:  # condição para solução do valor 3 
	print(f'O valor \033[1;34m3\033[m pareceu na \033[1;34m{num.index(3) + 1}ª\033[m posição. ')
else:
	print(f'O valor \033[1;34m3\033[m não foi digitado. ')
print(f'Os valores pares digitados ', end='')
for n in num:  # mostra os valores pares
	if n % 2 == 0:
		print(f'\033[1;34m{n}\033[m ', end='')
print('\n{:-^40}'.format('FIM'))
