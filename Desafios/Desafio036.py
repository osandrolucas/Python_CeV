print("""Escreva um programa para aprovar o empréstimo bancário de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quntos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela n~~ao pode exceder 30% do salário ou então o  empréstimo será negado""")

valor_casa = float(input('\nQual o valor da casa: R$'))
salario = float(input('Qual o seu salário: R$'))
anos = int(input('Em quantos anos você vai pagar? R$'))
minimo = salario * 30 / 100
prestacoes = valor_casa / (anos * 12)

print('\nPara pegar uma casa de R${:.2f} em {} anos a prestação será de R$ {:.2f} e ele ultrapassa 30% do valor do seu salário.'.format(valor_casa, anos), end='')
print('a prestação será de R$ {:.2f}'.format(prestacoes))

if prestacoes <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!!')