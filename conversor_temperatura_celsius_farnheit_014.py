'''entre no sistema com a temperatura em Celsius e tranforme
ela em Fahrenheit'''
cel = float(input('Digite a temperatura e Graus Centigrado: '))
far = cel * (9 / 5) + 32 # formúla para fahrenheit
print(F'Celsius = \033[1;34m{cel:.1f}Cº\033[m seu valor em Fahrenheit = \033[1;34m{far:.1f}Fº\033[m')
