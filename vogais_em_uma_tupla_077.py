'''crie uma tupla com varias palavras processe ela e mostre quais as suas vogais'''
frase = ('bonito', 'verdade', 'confiar', 'acima', 'tudo', 
	     'mente', 'positiva', 'sempre', 'ocupando', 'cabeça',
	     'preenche', 'qualquer', 'vazio', 'almas', 'livres', 
	     'entende', 'valor', 'continuar', 'assim')
for f in frase:
	print(f'\nNa palavra {f.upper()} temos ', end='')
	for letra in f:
		if letra.lower() in 'aeiou':
			print(f'\033[1;31m{letra}\033[m', end=' ')
print('\nFIM')