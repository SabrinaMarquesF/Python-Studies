real = float(input('Quanto de dinheiro você possui na carteira?'))
dolar = real / 5.12
euro = real / 5.3
kwanza = real / 0.012
print('Voê poderá comprar com R${}, {:.2f} dólares, {:.2f} euros e {:.2f} kwanzas'.format(real, dolar, euro, kwanza))
