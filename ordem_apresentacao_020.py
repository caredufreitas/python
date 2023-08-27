'''entre no sistema o nome de quatro alunos e saia com uma ordem 
aleatória escolhida pelo sistema'''

from random import shuffle
print('{:-^40}'.format('APRESENTAÇÃO ALEATÓRIA'))
aluno_01 = str(input('Digite o nome do Aluno 01: ')).strip().capitalize()
aluno_02 = str(input('Digite o nome do Aluno 02: ')).strip().capitalize()
aluno_03 = str(input('Digite o nome do Aluno 03: ')).strip().capitalize()
aluno_04 = str(input('Digite o nome do Aluno 04: ')).strip().capitalize()
alunos = list([aluno_01, aluno_02, aluno_03, aluno_04])
shuffle(alunos)
print(f'\033[1;34mOrdem dos Alunos.\n{alunos}\033[m')
print('{:-^40}'.format('FIM'))

