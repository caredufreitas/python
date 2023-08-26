'''entre no programa com o dia, mês, ano de uma pessoa
saida com a data formatada dando uma mensagem de boas vindas! '''

from datetime import date
data = date.today()
print('Bem vindo! {}'.format(data))
dia = int(input('Informe o Dia que você nasceu? '))
mes = str(input('Informe o Mês que você nasceu [Ex: Jan]? '))
ano = int(input('Informe o ano em que você nasceu? '))
print('Olá, você nasceu no dia {} de {} de {}. '.format(dia, mes, ano))

