'''entre no sistema o valor de três retas e saia com uma mensagem 
se os valores podem formar um triângulo'''
r1 = int(input('Digite o valor da 1ª reta: '))
r2 = int(input('Digite o valor da 2ª reta: '))
r3 = int(input('Digite o valor da 3ª reta: '))
print(f'Os valores \033[1;34m[{r1}]\033[m, \033[1;34m[{r2}]\033[m, \033[1;34m[{r3}]\033[m →', end=' ')
if(r1 < r2 + r3) and (r2 < r3 + r1) and (r3 < r2 + r1):
	print('\033[1;34mPodem formar um Triângulo!\033[m ')
else:
	print('\033[1;34mNão podem formar um Triângulo!\033[m ')
print('{:-^40}'.format('FIM'))