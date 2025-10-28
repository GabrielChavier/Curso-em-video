preço = float(input('Qual o preco do seu produto'))
novo = preço - (preço * 5 / 100)
print('O produto que custava RS{:.2f}, na promoção vai custan RS{:.2f} com desconto.'.format(preço, novo))
