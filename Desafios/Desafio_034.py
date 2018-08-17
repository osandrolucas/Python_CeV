print("""Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
Para salários superiores a R$1250,00, calcule um aumento de 10%. 
Para os inferiores ou iguais, o aumento é de 15%.\n""")

sal = float(input('Qual seu salário: R$ '))

if sal > 1250:
    novo = ((sal*10)/100) + sal
    a = '10%'
if sal <= 1250:
    novo = ((sal*15)/100) + sal
    a = '15%'

print('Seu antigo salário era {:.2f} e com aumento de {} ficou {:.2f}, Parabéns!'.format(sal, a, novo))