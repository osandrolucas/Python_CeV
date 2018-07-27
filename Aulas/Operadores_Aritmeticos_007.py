#Esta é a ordem de precedencia
#1. ()
#2. **
#3. * / // % ... Obs.: / Divisão, // Divisão inetira
#4. + -
#Obs.: Potência: Posso fazer 4**3 ou pow(4,3)

#O limite é o tamanho da memória
print('Exemplos')
print('Oi * 5 é ','Oi' * 5)
print('= * 20 é ','='*20)
nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:#^10}!'.format(nome))
#Para centralizar --> {:^20}
#Para Direita --> {:>20}
#Para Esquerda--> {:<20}
#Para preencher com 0 a direita por exemplo: {:0>20}
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1+n2
m = n1*n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d),end=' ')
print('A divisão inteira é {} e potência {}'.format(di, e))
#.end' ' para não quebrar a linha e colocar um espaço
#\n quebra a linha