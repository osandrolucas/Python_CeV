print('===Convertendo para float===')
n = float(input('Digite um valor: '))
print('Em float este número fica {}'.format(n))
print(type(n))

b = input('Digite outra coisa...')
print('Is numérico? ',b.isnumeric()) #Informa se é numerico
print('Is Letra/Alpha?',b.isalpha()) #Informa se é Letra
print('Is alfanumérico? ',b.isalnum()) #Informa se é alfanumérico 1a
print('Está em minusculo? ', b.islower())
print('Está em maisculo?', b.isupper())