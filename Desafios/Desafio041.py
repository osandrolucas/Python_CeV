from datetime import date

print('''DESAFIO 041\nA confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
--> Até 9 anos: MIRIM
--> Até 14 anos: INFANTIL
--> Até 19 anos: JUNIOR
--> Até 25 anos: SÊNIOR
--> Acima: MASTER\n''')

ano_nasc = int(input('Ano de Nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('O atleta tem {} anos'.format(idade))

if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JUNIOR')
elif idade <= 25:
    print('Classificação: JUNIOR')
else:
    print('Classificação: MASTER')