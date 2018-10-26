print('''EXERCICIO 32 \nEscreva um proframa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão.
1 - Binário\n2 - Octal\n3 - Hexadecimal''')

num = int(input('Escreva um número inteiro qualquer: '))
#Converter o número para uma das opções abaixo.

print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua opção: '))

if op == 1:
    print('\nO número {} em BINÁRIO é {}.'.format(num, bin(num)[2:]))
elif op == 2:
    print('\nO número {} em BINÁRIO é {}.'.format(num, oct(num)[2:]))
elif op == 3:
    print('\nO número {} em BINÁRIO é {}.'.format(num, hex(num)[2:]))
else:
    print('\nOpção inválida. Tente novamente.')