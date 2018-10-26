print('''Exercicio 40\nCrie um programa que leia duas notas de um aluno e calcule a média, mostrando uma mensagem no final de acordo com a média atingida.
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- MÉDIA 7.0 ou superior: APROVADO\n''')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

media = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1, n2, media))
if 7 > media >= 5:
#if media >= 5 and media < 7
    print('O aluno está em RECUPERAÇÃO.')
elif media < 5:
    print(print('O aluno está em REPROVADO.'))
else:
    print('O aluno está APROVADO.')
