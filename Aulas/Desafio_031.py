print("""Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, 
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.""")
km = float(input('Qual a distância da viagem em Km?'))
print('Você está prestes a começar uma viagem de {}km'.format(km))
if km <= 200.00:
    preco = km * 0.50
else:
    preco = km * 0.45
print('Preço da viagem: R${:.2f}'.format(preco))

#If inline / Operador Ternário
#preco = km * .050 if km<= 200 else km * 0.45
