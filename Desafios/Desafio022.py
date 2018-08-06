print("""Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas;
– Quantas letras ao todo (sem considerar espaços);
– Quantas letras tem o primeiro nome.\n""")

nome = str(input('Nome: '))
print('O nome em maiúsculo: {}'.format(nome.upper()))
print('O nome em minúsculo: {}'.format(nome.lower()))
print('Qual o tamanho do nome sem considerar espaços? {}'.format(len(nome) -nome.count(' ')))
dividido = nome.split()
print('Quantas letras tem o primeiro nome? {}'.format(len(dividido[0])))

