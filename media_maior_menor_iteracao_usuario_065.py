'''entre no programa vários valores inteiros saia com sua média, maior, menor valor que foi
lido iteragindo com usuário se ele precisa adicionar mais valores '''
resp = 'S'
total = media = cont = maior = menor = 0
print('{:-^40}'.format('ANÁLIDE DE NÚMEROS INSERIDOS'))
while resp in 'S':
	num = int(input('Digite um número: '))
	cont += 1
	total += num
	if cont == 1:
		maior = num
		menor = num
	else:

		if num > maior:
			maior = num
		if num < menor:
			menor = num
	resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
media = total / cont
print(f'Foi \033[1;32m{cont}\033[m número digitado e sua média é \033[1;32m{media:.1f}\033[m. ')
print(f'Tendo \033[1;32m{maior}\033[m como maior e \033[1;32m{menor}\033[m como menor número lido. ')
print('{:-^40}'.format('FIM'))
