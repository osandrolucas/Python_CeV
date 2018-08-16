print("""Exercício Python 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.""")
from datetime import date
from emoji import emojize

ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
    print('Ano atual: {}'.format(ano))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO {}'.format(ano, emojize(':relaxed:', use_aliases=True)))
else:
    print('O ano {} NÃO é BISSEXTO {}'.format(ano, emojize(':pensive:', use_aliases=True)))


