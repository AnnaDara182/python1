#Cumprimento para o  cliente
print('Bem vindo(a) a loja da Anna Dara Moraes Araujo')

#Variaveis para valor da compra e a quantia de parcelas
valorDoPedido = float(input('Digite o valor do pedido: '))
quantidadeDeParcelas = int(input('Em quantas vezes gostaria de parcelar? '))

#Valor das parcelas e taxa de juros
if quantidadeDeParcelas < 4 :
    juros = (0/100)
elif (quantidadeDeParcelas >= 4 ) and (quantidadeDeParcelas < 6 ):
   juros = (4/100)
elif (quantidadeDeParcelas >= 6 ) and (quantidadeDeParcelas < 9 ):
   juros = (8/100)
elif (quantidadeDeParcelas >= 9 ) and (quantidadeDeParcelas < 13 ):
    juros = (16/100)
else:
   juros = (32/100)

#Calculo da parcela
valorDaParcela = (valorDoPedido * (1 + juros) / quantidadeDeParcelas)
print(f'O valor de cada parcela é de: {valorDaParcela:.2f}')

#Calculo do valor total parcelado
valorTotalParcelado = (valorDaParcela * quantidadeDeParcelas)
print(f'O valor total parcelado é de: {valorTotalParcelado:.2f}')