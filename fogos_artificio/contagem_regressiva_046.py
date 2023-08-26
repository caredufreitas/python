'''simule uma contagem regressiva para estouro de fogos de artificio indo de 10 à 0 com uma pausa
de 1 segundo entre eles mostre um emoji'''
import emoji
from time import sleep

print(emoji.emojize('Contagem Regressiva :grin:', use_aliases=True))
for i in range(10, -1, -1):
	print(i)
	sleep(1)
print(emoji.emojize(':boom:  :boom:  :boom:', use_aliases=True), end=' ')
print('Fim')
