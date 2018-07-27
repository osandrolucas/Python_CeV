#Faça um algoritimo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento
salario = float(input('Informe seu salário ... R$ '))
novo_salario = salario + (salario*15/100)
print('Seu salário de R$ {:.2f} teve aumento de 15% e passou a ser R$ {:.2f}'.format(salario, novo_salario))