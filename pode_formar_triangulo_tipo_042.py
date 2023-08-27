'''entre com três seguimentos de retas processe se forma um triângulo e mostre
que tipo de triângulo elas podem formar, Equilátero os três seguimentos iguais, 
isóceles dois lados iguais, Escaleno todos os lados diferentes'''
print('{:-^40}'.format('ANÁLISADOR DE TRIÂNGULOS'))
r1 = int(input('Digite o seguimento da Reta 01: '))
r2 = int(input('Digite o seguimento da Reta 02: '))
r3 = int(input('Digite o seguimento da Reta 03: '))
print(f'Os seguimentos \033[1;34m[{r1}]-[{r2}]-[{r3}]\033[m → ', end='')
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
	print('\033[1;34mPodem forma um Triângulo.\033[m ', end='')
	if r1 == r2 and r1 == r3 and r2 == r3 and r2 == r1 and r3 == r1 and r3 == r2:
		print('\033[1;33mEquilátero.\033[m ')
	elif r1 != r2 and r1 != r3 and r2 != r3 and r2 != r1 and r3 != r1 and r3 != r2:
		print('\033[1;33mEscaleno.\033[m ')
	else:
		print('\033[mIsóceles.\033[m ')
else:
	print('\033[1;31mNão podem formar um Triângulo.\033[m ')
print('{:-^40}'.format('FIM'))
