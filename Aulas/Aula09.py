frase = 'Curso em Vídeo Python'
print(frase)
print('Somente a terceira letra: ',frase[3])
print('Do inicio até o 13: ',frase[3:13])
print('Do inicio até o 15 de 2 em 2: ',frase[3:15:2])
print('Escrevendo texto longo usando """ ')
print("""Aqui é Body Builder Ipsum! Eu quero esse 13 daqui a pouquinho aí. 
Tá saindo da jaula o monstro! Sabe o que é isso daí? 
   Trapézio descendente é o nome disso aí. É verão o ano todo vem cumpadi. 
      Aqui nóis constrói fibra, não é água com músculo. Não vai dá não. 
         É esse que a gente quer, é ele que nóis vamo buscar. Boraaa, Hora do Show.""")
print('Quantas vezem tem o (minusculo)? {}'.format(frase.count('o')))
print('Quantas vezem tem o (maiusculo)? {}'.format(frase.upper().count('O')))
print('Qual o tamanho de {} ? {}'.format(frase, len(frase.strip())))
print('Troca Python por Android: {} '.format(frase.replace('Python','Android')))
#O replace não muda efetivamente
print('A palavra curso está dentro da frase? {}'.format(frase.find('Curso')))
print('Frase splitada (dividida): {}'.format(frase.split()))
dividido = frase.split()
print('Primeiro item da lista: {}'.format(dividido[0]))
print('Dentro de Video, qual é a letra 3? {}'.format(dividido[2][3]))