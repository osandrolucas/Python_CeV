print('''EXERCICIO 38\nEscreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não Existe avlor maior, os dois são iguais''')

print('\nInforme dois valores que eu direi qual o maior valor, se é que existe....')
n1 = int(input('Informe o primeiro número inteiro: '))
n2 = int(input('Informe o segundo número inteiro: '))

if n1 > n2:
    print('\nO PRIMEIRO número é maior --> {}'.format(n1))
elif n2 > n1:
    print('\nO SEGUNDO número é maior --> {}'.format(n2))
else:
    print('\nOs dois números são IGUAIS --> {} e {}'.format(n1, n2))
