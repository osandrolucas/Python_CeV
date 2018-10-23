print("""Escreva um programa para aprovar o empréstimo bancário de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quntos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela n~~ao pode exceder 30% do salário ou então o  empréstimo será negado""")

valor_casa = float(input('\nQual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Em quantos anos você vai pagar? '))

#Calculando valor da prestação da casa
prestacoes = valor_casa / anos

if float(prestacoes) > (salario * 0.3):
    print('\nInfelizmente você não pode financiar esta casa. O valor da parcela ficou em R$ {} e ele ultrapassa 30% do valor do seu salário.'.format(salario * 0.3))
else:
    print('Financiamento APROVADO!')
    print('As prestações da casa serão no valor de R$ {:.3f} ao mês.'.format(prestacoes))