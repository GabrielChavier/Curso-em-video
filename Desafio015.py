#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidde de dias pelos quais ela foi alugado. calcule o preço a pagar, sabendo que o carro custa rs60 por dia e rs0,15 por km rodado
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados?' ))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar e de RS{:.2f}'.format(pago))
