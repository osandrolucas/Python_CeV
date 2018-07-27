#Crie um porgrama que leia um número real qualquer pelo teclado e mostre na tela sua porção inteira
#Ex: Digite 6.127, exiba 6

from math import trunc
num = float(input('Informe um valor flutuante, por exemplo, 6.127 -->  '))
inte = trunc(num)
print('Número Flutuante {} tem a parte inteira {}!'.format(num, inte))