print("""Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela 
começa ou não com o nome "SANTO".""")
print('Meu jeito de fazer antes de ver a resposta....')
n_cidade = input('Escreva o nome de uma cidade: ')
d = n_cidade.split()
if d[0].upper() == 'SANTO':
    print('Começa com Santo')
else:
    print('Não começa com Santo')

print('Jeito de fazer Gustavo....')
cid = str(input('Escreva o nome de uma cidade: ')).strip() #Strip apaga espaços
print(cid[:5].upper() == 'SANTO')