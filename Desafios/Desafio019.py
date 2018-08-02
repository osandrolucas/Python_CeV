#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele. Lendo o nome deles e escrevendo o nome do escolhido.
from random import choice
print('Professor: Preciso de ajuda para apagar o quadro...')
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input ('Informe o nome do segundo aluno: '))
n3 = str(input('Informe o nome do terceito aluno: '))
n4 = str(input('Informe o nome do quarto aluno: '))
listaAlunos = [n1,n2,n3,n4]
escolhido = choice(listaAlunos)
print('O aluno escolhido foi: {}'.format(escolhido))