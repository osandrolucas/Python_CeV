print('''DESAFIO 042\nRefaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes''')

print('#*#' * 8)
print('ANALISADOR DE TRIÂNGULOS')
print('#*#' * 8)
r1 = float(input('\nInforme o primeiro segmento: '))
r2 = float(input('Informe o segundo segmento: '))
r3 = float(input('Informe o terceito segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar triângulo!')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar triângulo!')

