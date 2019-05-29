print('#'*3, 'ESTRUTURAS CONFICIONAIS ANINHADAS', '#'*3)
nome = str(input('Qual é seu nome? '))
if str.upper(nome) == 'LUCAS':
    print('Que nome bonito!')
elif str.upper(nome) == 'PEDRO' or str.upper(nome) == 'MARIA' or str.upper(nome) == 'PAULO':
    print('Seu nome é bem popular no Brasil.')
elif str.upper(nome) in ('ANA CLÁUDIA JÉSSICA JULIANA'):
    print('Belo nome feminino.')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia {}!'.format(nome))