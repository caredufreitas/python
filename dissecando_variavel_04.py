'''entre no sistema frase em string e mostre sua transformação e o tipo 
primitivo dela'''

frase = str(input('Digite algo? ')).strip()

print(f'Seu tipo primitivo - \033[1;34m{type(frase)}\033[m')
print(f'\033[1;34m{frase}\033[m - Contém - \033[1;34m{len(frase)}\033[m - caracteres.')
print(f'\033[1;34m{frase}\033[m - Caixa alta - \033[1;34m{frase.upper()}\033[m')
print(f'\033[1;34m{frase}\033[m - Em caixa baixa - \033[1;34m{frase.lower()}\033[m')
print(f'\033[1;34m{frase}\033[m - É um espaço - \033[1;34m{frase.isspace()}\033[m')
print(f'\033[1;34m{frase}\033[m - É Alpha - \033[1;34m{frase.isalpha()}\033[m')
print(f'\033[1;34m{frase}\033[m - È um Numérico - \033[1;34m{frase.isnumeric()}\033[m')
print(f'\033[1;34m{frase}\033[m - Está em caixa alta - \033[1;34m{frase.isupper()}\033[m')
print(f'\033[1;34m{frase}\033[m - Está em caixa baixa - \033[1;34m{frase.islower()}\033[m')
print(f'\033[1;34m{frase}\033[m - É um Alpha Númerico - \033[1;34m{frase.isalnum()}\033[m')

