print('#'*2,
    'Python – Fase 09 – Manipulando Strings','#'*2,
    '\nNessa aula, vamos aprender operações com String no Python...'
    '\nAs principais operações que vamos aprender são o Fatiamento de String, '
    'Análise com len(), count(), find(), \ntransformações com replace(), upper(), '
    'lower(), capitalize(), title(), strip(), junção com join().'
)

print('\nInfo: Para o python, toda cadeia de texto está entre aspas simples ou aspas duplas.'
     '\nSendo que, cadeia de caracteres significa nada mais nada menos que String\n'
)

print('IMPORTANTE: O Python diferencia maiuscula de minuscula!\n')

print('#'*2 ,'Fatiamento', '#' * 5)
print('Fatiar uma string é conseguir pegar partes de uma String')
frase = 'Curso em Video Python'
print('A frase: {}'.format(frase))

print('#'*2 ,'Exemplos de Manipulações', '#' * 5)
print('frase[9:21]  Vai do 9 até o 20 e não até o 21: {}'.format(frase[9:21]))
print('frase[9:21:2] Começa no 9, até o 21(20 no caso) pulando de 2 em 2: {}'.format(frase[9:21:2]))

print('frase[:5] Quando omito o inicio, começa do caracter 0, isto é (0:5): {}'.format(frase[:5]))
print('frase[15:] Quando omito o final, vai do inicio até o final: {}'.format(frase[15:]))
print('frase[9::3] Começa no 9, vai até o fim, pulando de 3 em 3: {}\n'.format(frase[9::3]))

print('#'*2 ,'Exemplos de Análises', '#' * 5)
print('Analisar uma String é saber algumas informações dessa String, como '
      'tamanho, primeira letra, essas coisas...')
print('Exemplo de len')
print('\nQual o comprimento da frase: {}'.format(len(frase)))
print('Exemplo de Count')
print('Quantas vezes aparece o? (minusculo): {}'.format(frase.count('o')))
print('Contagem já com fatiamento... {}'.format(frase.count('o',0,13)))
print('Exemplos de Find')
print('Em que posição começa a sigla "deo": {}'.format(frase.find('deo')))
print('Encontrar a palavra Android (que não existe): {}'.format(frase.find('Android')))
print('Exemplo de in')
print('Existe a palavra curso na frase? {}\n'.format('Curso' in frase))

print('#'*2 ,'Transformaçao', '#' * 5)
print('Via de regra não conseguimos mudar uma lista de String(Imutável) mas consiguimos mudar através de métdos')
print('Exemplo de Replace')
print('Substituir "Python" por "Android": {}\n'.format(frase.replace('Python','Android')))
print('O replace não muda efetivamente a String!!!')
print('Exemplo de Upper')
print('Deixando maíusculo: {}\n'.format(frase.upper()))
print('Exemplo de Lower')
print('Deixando maíusculo: {}\n'.format(frase.lower()))
print('Exemplo de Captalize')
print('Primeira maiuscula, o resto minúscula: {}\n'.format(frase.capitalize()))
print('Exemplo de Title')
print('Letras iniciam em maiusculo: {}\n'.format(frase.title()))

frase2 = '   Aprenda Python  '
print('Nova Frase que utilizaremos: {}'.format(frase2))
print('\nExemplo de Strip')
print('Exclui espaços que estão sobrando nas extremidades: {}\n'.format(frase2.strip()))
print('\nExemplo de Rstrip')
print('Exclui espaços que estão sobrando no lado direito da frase: {}\n'.format(frase2.rstrip()))
print('\nExemplo de Lstrip')
print('Exclui espaços que estão sobrando no lado esquerdo da frase: {}\n'.format(frase2.lstrip()))

print('#'*2 ,'Exemplos de Divisões', '#' * 5)
print('A frase é {}'.format(frase))
print('\nExemplo de Split')
print('Divide a string em listas a cada espaço... {}'.format(frase.split()))
frase = frase.split()
print('\nExemplo de Join')
print('Juntando a string separando os caracteres por um traço... {}'.format('-'.join(frase)))


#varia = str(input('Escreva qualquer coisa que substituirei por Nabucodonosor: '))
#qualquer = format(varia.replace(varia,'Nabucodonosor'))
#print('{}'.format(qualquer))