#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
celsius = float(input('Informe a temperatura em graus Celsius ...'))
fa = ((9 * celsius) / 5) + 32 #Não precisava de parenteses
print('A temperatura de {0}°C equivale a {1}°F!'.format(celsius,fa))