print("""Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.""")
frase = str(input('Dite uma frase: ')).upper().strip() #remove espaços indesejados
print('A letra "A" aparece {} vezes na frase'.format(frase.upper().count('A')))
print('A letra "A" aparece pela primeira vez na posição {}'.format(frase.find('A')+1))
print('A letra "A" aparece pela ultima vez na posição {}'.format(frase.rfind('A')+1))
