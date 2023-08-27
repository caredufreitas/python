'''entre no sistema com quatro nome de aluno saia com um escolhido'''
from random import choice
print('{:-^40}'.format('SORTEIO'))
aluno_01 = str(input('Digite o nome do Aluno 01: ')).strip().capitalize()
aluno_02 = str(input('Digite o nome do Aluno 02: ')).strip().capitalize()
aluno_03 = str(input('Digite o nome do Aluno 03: ')).strip().capitalize()
aluno_04 = str(input('Digite o nome do Aluno 04: ')).strip().capitalize()
alunos = list([aluno_01, aluno_02, aluno_03, aluno_04]) # cria uma lista de alunos
sorteado = choice(alunos)  # choice é um interator ou seja precisa de uma interface para mostrar
print(f'O sorteado é \033[1;34m{sorteado}\033[m')
print('{:-^40}'.format('FIM'))


