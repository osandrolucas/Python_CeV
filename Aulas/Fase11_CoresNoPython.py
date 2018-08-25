#Coleções criadas para facilitar
cores = {'limpa': '\033[m',
         'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'magenta': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'pretoebranco': '\033[7;30m'
         }

estilos = {
    'none': '\033[m',
    'bold': '\033[1m',
    'underline': '\033[4m',
    'negative': '\033[m',
    'limpa': '\033[m'
}

back = {
        'limpa': '\033[m',
        'branco': '\033[40m',
        'vermelho': '\033[41m',
        'verde': '\033[42m',
        'amarelo': '\033[43m',
        'azul': '\033[44m',
        'magenta': '\033[45m',
        'ciano': '\033[46m',
        'cinza': '\033[47m',

}

print('{}###{} {}Cores{} {}no{} {}Python{} {}###{}'.format(cores['vermelho'], cores['limpa'], cores['verde'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa'], cores['ciano'], cores['limpa']))

print(
    "Padrão: \033[SStyle;Text;Backm"
)


print(str.upper('\nExemplos de Style....'))
print('Código 0 - {}None (Nada){}'.format(estilos['none'], estilos['limpa']))
print('Código 1 - {}Bold (Negrito){}'.format(estilos['bold'], estilos['limpa']))
print('Código 4 - {}Underline (Sublinhado){}'.format(estilos['underline'], estilos['limpa']))
print('Código 7 - {}Negative (Negativo){}'.format(estilos['negative'], estilos['limpa']))

print(str.upper('\nExemplos de Cores....'))
print('Código 30 - {}White (Branco){}'.format(cores['branco'], cores['limpa']))
print('Código 31 - {}Red (Vermelho){}'.format(cores['vermelho'], cores['limpa']))
print('Código 32 - {}Green (Verde){}'.format(cores['verde'], cores['limpa']))
print('Código 33 - {}Yellow (Amarelo){}'.format(cores['amarelo'], cores['limpa']))
print('Código 34 - {}Blue (Azul){}'.format(cores['azul'], cores['limpa']))
print('Código 35 - {}Magenta (Magenta){}'.format(cores['magenta'], cores['limpa']))
print('Código 36 - {}Cyano - (Ciano){}'.format(cores['ciano'], cores['limpa']))
print('Código 37 - {}Grey (Cinza){}'.format(cores['cinza'], cores['limpa']))

print('\nExemplos de Backgrounds....')
print('Código 40 - {}White (Branco){}'.format(back['branco'],back['limpa']))
print('Código 41 - {}Red (Vermelho){}'.format(back['vermelho'],back['limpa']))
print('Código 42 - {}Green (Verde){}'.format(back['verde'],back['limpa']))
print('Código 43 - {}Yellow (Amarelo){}'.format(back['amarelo'],back['limpa']))
print('Código 44 - {}Blue (Azul){}'.format(back['azul'],back['limpa']))
print('Código 45 - {}Magenta (Magenta){}'.format(back['magenta'],back['limpa']))
print('Código 46 - {}Cyano - (Ciano){}'.format(back['ciano'],back['limpa']))
print('Código 47 - {}Grey (Cinza){}'.format(back['cinza'],back['limpa']))


print('\nPraticando...')
print('\033[0;30;41m Sem formatação especial - Letra Branca - Fundo Vermelho\033[m')
print('\033[4;33;44m #Sublinhado - Letra Amarela - Fundo Azul\033[m')
print('\033[1;35;43m #Negrito - Letra Magenta - Fundo Amarelo\033[m')
print('\033[30;42m #Sem formatação especial - Letra Branca - Fundo Verde\033[m')
print('\033[m #Sem configuração, padrão do terminal (Fundo Preto, letra cinza)\033[m')
print('\033[7;30m Letra Preta - Fundo Branco\033[m')

print('\n\n\033[4;30;45mOlá Mundo!\033[m')
print('\n\n\033[7;30mOlá Mundo!\033[m')
print('\n\n\033[7mOlá Mundo!\033[m')
a = 3
b = 5
print('\nOs valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

nome = 'Lucas'
print('Olá, muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

print('Exemplo usando coleção --> Olá, muito prazer, {}{}{}!!!'
      .format(cores['pretoebranco'], nome, cores['limpa']))
