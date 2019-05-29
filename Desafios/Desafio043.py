print("""\nExercício Python 043: \n\nDesenvolva uma lógica que leia o pedo e a altura de uma pessoa, calcule seu IMC e mostre 
o status de acordo com a tabela abaixo.\n
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
""")

def calcula_imc(peso, altura):
    imc = peso / (altura + altura)
    print(peso)
    print(altura)
    ##print(imc)

print('#'*3, 'BEM VINDO A CALCULADORA DE IMC', '#'*3)
nome = str(input('Olá. Qual o seu nome? '))
peso = float(input('{}, Qual o seu peso em Kg? \nExemplo: 70.00 ....: '.format(str.capitalize(nome))))
altura = float(input('E qual a sua altura em cm? \nExemplo: 170 ....: '))
calcula_imc(peso, altura)



