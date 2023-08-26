'''entre no programa com um valor qualquer e mostre seu fatorial'''
print('{:-^40}'.format('FATORIAL'))
num = int(input('Quer ver o fatorial de que número? '))
print(f'\033[1;34m{num}!\033[m', end=' ')
fact = 1
while num > 0:
	fact *= num  # processa o fatorial
	print(f'\033[1;33m{num}x\033[m ', end='')
	num -= 1  # decrementa 1 no num
print(f'= \033[1;34m{fact}\033[m')
print('\n{:-^40}'.format('FIM'))
