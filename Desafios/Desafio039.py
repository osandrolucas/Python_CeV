from datetime import date

print('''EXERCICIO 39\nFaça um programa que leia a data de nascimento de um jovem e informe, de acordo com a sua idade
- Se ele ainda vai ter que se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do .
''')

ano = int(input('\nAno de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano
alistamento = idade + (idade - 18)
print('Quem nasceu em {} tem {} em {}'.format(ano, idade, ano_atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}'.format(ano_atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format( ano_atual - saldo))
