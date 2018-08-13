print("""\nExercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro 
e o último nome separadamente.""")
nome = str(input('Informe seu nome completo: ')).strip()
print('\nMuito prazer em te conhecer!')
nome_d = nome.split()
print('Seu primeiro nome é: {}'.format(nome_d[0]))
print('Seu último nome é: {}'.format(nome_d[len(nome_d)-1]))
