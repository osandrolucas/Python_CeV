#Crie um algoritmo que leia um numero e mostre seu dobro, triplo e raiz quadrada

import math
n1 = int(input('Informe um número: '))
print('O número informado foi --> {} \n Seu Dobro: {} '
      '\n Seu Triplo: {}'.format(n1, n1*2, n1*3))
print('Raiz quadrada Jeito 1: {}'.format(n1**(1/2)))
print('Raiz quadrada Jeito 2: {}'.format(math.sqrt(n1)))
