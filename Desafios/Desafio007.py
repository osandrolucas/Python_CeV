#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média
n1 = float(input('Informe a Nota 1: '))
n2 = float(input('Informe a Nota 2: '))
media = (n1+n2) / 2
print('A média entre {:.1f} e {:.1f} é {}'.format(n1,n2,media))