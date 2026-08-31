#Peça o valor de uma compra e informe se ela é elegível para desconto (valor maior que R$100).

purchase = float(input("Purchase price: "))

if purchase > 100:
    print("Purchase eligible for a discount")