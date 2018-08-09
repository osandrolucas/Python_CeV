print("""Exercício Python 023: Faça um programa que leia um número de 0 a 9999 e mostre na
tela cada um dos dígitos separados.""")

num = int(input('Escreva um número de 0 a 9999: '))
if num >= 9999:
    print('O número deve ser até 9999! Tchau pra ti.')
if num < 0:
    print('O número deve ser maior ou igual a 0! Tchau pra ti.')
print('Analisando o número {}'.format(num))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

if u == 0:
    print('Unidade: Não possui unidade')
else:
    print('Unidade: {}'.format(u))

if d == 0:
    print('Dezena: Não possui dezena')
else:
    print('Dezena: {}'.format(d))

if c == 0:
    print('Centena: Não possui centena')
else:
    print('Centena: {}'.format(c))

if m == 0:
    print('Milhar: Não possui milhar')
else:
    print('Milhar: {}'.format(m))
