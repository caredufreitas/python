'''entre no programa com um angulo qualquer e mostre na tela o valor do seno,
cosseno, tangente desse angulo'''

from math import radians, sin, cos, tan
cores = {'limpa': '\033[m', 'vermelho': '\033[1;31m'}
print('{:-^40}'.format('SENO | COSENO | TANGENTE | RADIANOS'))
angulo = int(input('Digite um Ângulo: '))
print(cores['vermelho'])
print(f'Ângulo = {angulo}º\nRadianos = {radians(angulo):.2f}\nSeno = {sin(radians(angulo)):.2f} ')
print(f'Coseno = {cos(radians(angulo)):.2f}\nTangente = {tan(radians(angulo)):.2f} ')
print(cores['limpa'])
print('{:-^40}'.format('FIM'))

