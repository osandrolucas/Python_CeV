#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seu seno, cosseno e tangente desse angulo.
#existem bibliotecas faceis
import math
print('Resolvendo somente com a Matemática')
âng = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(âng)) #Pega o ângulo e converte para radianos
print('O ângulo de {} tem o SENO de {:.2f}'.format(âng, seno))
cosseno = math.cos((math.radians(âng)))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(âng, cosseno))
tangente = math.tan(math.radians(âng))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(âng, tangente))
