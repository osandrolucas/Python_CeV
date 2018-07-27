#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais
#  ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Informe a quantidade de Km percorridos: '))
dias = int(input('Quantidade de dias do aluguel: '))
preco = (dias * 60) + (km * 0.15)
print('Você rodou {:.2f}Km por {} dias. O preço final é R${:.2f}'.format(km,dias,preco))