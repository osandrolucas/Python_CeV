import random

print(""""Escreva um programa que faça o computador 'pensar' em um número inteiro de 0 a 5
           e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
           
           O programa deverá escrever na tela se o usuário venceu ou perdeu.""")
print('Pensei em um número....')
n = (random.random())
print(n)
chute = int(input('Chute: De 1 a 5, qual número você acha que pensei? '))

if chute == n:
    print('Parabéns! Você acertou, o número que escolhi foi {}!'.format(n))
else:
    print('Infelizmente tu errou.... Tente novamente')
