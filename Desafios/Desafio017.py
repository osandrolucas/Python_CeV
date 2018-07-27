#FUP que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa
print('Maneira com Conceito Matemático!')
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))

from math import hypot
print('\nManeira utilizando a Math')
cos = float(input('Comprimento do cateto oposto: '))
cat = float(input('Comprimento do cateto adjacente: '))
hip = hypot(cos , cat)
print('A hipotenusa vai medir {:.2f}'.format(hip))