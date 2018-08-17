print("""Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas
 podem ou não formar um triângulo.\n""")

print('#*#' * 8)
print('ANALISADOR DE TRIÂNGULOS')
print('#*#' * 8)
r1 = float(input('\nInforme o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceito segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')