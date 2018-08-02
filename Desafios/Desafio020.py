#O mesmo professor do desafio anterior, quer sortear a ordem da apresentação de trabalhos dos alunos.
#FUP que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random as a #alias
print('Informe os nomes dos alunos que apresentarão o trabalho: ')
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = str(input ('Informe o nome do segundo aluno: '))
n3 = str(input('Informe o nome do terceito aluno: '))
n4 = str(input('Informe o nome do quarto aluno: '))
lista = [n1,n2,n3,n4]
a.shuffle(lista) #embaralhando
input('A ordem de apresentação será {}'.format(lista))