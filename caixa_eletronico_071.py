'''simulacao de um caixa eletronic entre com valor para saque considere 
cédulas de R$50, R$20, R$20, R$1'''
print('#' * 22)
print('# INTERNATIONAL BANK #')
print('#' * 22)
valor = int(input('Valor de Saque R$'))
total = valor  # atribui um montante
cedula = 50
total_cedulas = 0
while True:
    if total >= cedula:  # relaciona toda vez que a cedula muda
        total -= cedula  # vai subtrai do total
        total_cedulas += 1
    else:
        if total_cedulas > 0: # condicao para nao mostrar cedulas com 0
            print(f'Total de \033[1;34m{total_cedulas}\033[m cédulas de \033[1;34mR$:{cedula}\033[m reais.')
        if cedula == 50:  # verificando a cédula atual
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        total_cedulas = 0  # zera o total de cedulas para mostrar na tela

        if total == 0:  # sai do loop
            break
print('#' * 37)
# operacao realizada com sucesso
print('# Operation performed successfully #')
print('#' * 37)