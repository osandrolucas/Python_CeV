#Faça um programa que leia o preço de um produto e mostre seu novo preço com 5% de desconto
preco = float(input('Preço do produto ... R$ '))
novo_preco = preco - (preco*5/100)
print('O produto custava R$ {} e o novo preço com 5% de desconto é R${:.1f}'.format(preco, novo_preco))