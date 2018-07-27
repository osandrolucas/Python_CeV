from math import sqrt, ceil, floor
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz quadradede {} é {}. \nArredondado para cima fica: {}\nArredondado para baixo fica: {}'.format(num,raiz, ceil(raiz),floor(raiz)))

