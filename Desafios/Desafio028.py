from random import randint

print(""""Escreva um programa que faça o computador 'pensar' em um número inteiro de 0 a 5
           e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
           
           O programa deverá escrever na tela se o usuário venceu ou perdeu.""")
print('-=-' * 20 )
print('Pensei em um número....')
print('-=-' * 20 )
n = randint(0,5) #Computador pensa de 0 a 5
chute = int(input('Chute: De 1 a 5, qual número você acha que pensei? '))

if chute == n:
    print('Parabéns! Você acertou, eu pensei no número {}!'.format(n))
else:
    print('Infelizmente tu errou.... Eu pensei no número {} e não {}.'.format(n,chute))
