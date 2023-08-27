'''entre no programa com um valor inteiro e saia com uma mensagem 
se o valor é para ou impar'''
print('{:-^40}'.format('PAR OU IMPAR'))
num = int(input('Digite um valor: '))
print(f'{num}', end='→ ')
print('\033[1;34mPAR\033[m' if num % 2 == 0 else '\033[1;34mIMPAR\033[m')
print('{:-^34}'.format('FIM'))
