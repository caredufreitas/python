'''entre no programa com pese e altura de uma pessoa calcule o imc mostre
abaixo 18.5 abaixo do pesso, entre 18.5 e 25 peso ideal, 25 à 30 sobrepeso, 30 à 40 obesidade
acima obesidade mórbida'''
print('{:-^40}'.format('CÁLCULO IMC'))
altura = float(input('Digite sua altura em (Mtr): '))
peso = float(input('Digite seu peso e (Kl): '))
imc = peso / (altura ** 2)
print(f'IMC: \033[1;32m{imc:.2f}\033[m e seu status é ', end='')
if imc <= 18.5:
	print('\033[1;31mABAIXO DO PESO.\033[m ')
elif 18.5 > imc <= 25.0:
	print('\033[1;32mPESO IDEAL.\033[m ')
elif 25.0 > imc <= 30.0:
	print('\033[1;31mSOBREPESO.\033[m ')
elif 30 > imc <= 40:
	print('\033[1;31mOBESIDADE.\033[m ')
else:
	print('\033[1;31mOBESIDADE MÓRBIDA.\033[m ')
print('{:-^40}'.format('FIM'))
