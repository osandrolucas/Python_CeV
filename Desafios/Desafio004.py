print('--- Informe dois numeros e exiba a soma dos dois')
num1 = input('Digite um numero:')
num2 = input('Digite outro numero:')
soma2 = int(num1)+int(num2)
print('A soma entre {0} e {1} é {2}'.format(num1, num2, soma2)) #0 1 e 2 não são obrigatórios
print('===Exemplo com Inteiro===')
n1 = int(input('Infome um número: '))
n2 = int(input('Informe outro número: '))
soma = n1+n2
print('A soma destes 2 números é {}'.format(soma))

b = input('Digite outra coisa...')
print('Is numérico? ',b.isnumeric()) #Informa se é numerico
print('Is Letra/Alpha?',b.isalpha()) #Informa se é Letra
print('Is alfanumérico? ',b.isalnum()) #Informa se é alfanumérico 1a
print('Está em minusculo? ', b.islower())
print('Está em maisculo?', b.isupper())