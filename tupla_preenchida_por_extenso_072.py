'''preencha um tupla por extenso com o nome dos números de 0 à 20, entre com um
valor pelo teclado entre (0 e 20) e saia com o valor que ele se encontra na tupla'''
print('{:-^40}'.format('NÚMERO POR EXTENSO'))
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 
	'Cinco', 'Seis', 'Sete', 'Oito', 'Nove',
	'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 
	'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
	'Dezenove', 'Vinte')  # substitui os condições as vezes
op = 'S'
while op in 'S':	
	while True:
		num = int(input('Digite um número entre 0 e 20: '))
		if 0 <= num <= 20:  # condicao de parada (0 é maior ou igual que -1 - (F), 20 menor ou igual 21 - (F))
			break		
		print('Tente novamente. ', end='')	
	print(f'Voçê digitou o número \033[1;32m{cont[num]}\033[m')
	op = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
print('{:-^40}'.format('FIM'))
