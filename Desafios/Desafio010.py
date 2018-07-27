#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
#Considere: US$1 = R$ 3,27

valor = float(input('Quantos reais você tem?'))

print('Com R${:.2F} pode comprar US${:.2f} dolares!'.format(valor,valor/3.27))