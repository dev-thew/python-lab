#Peça o valor da compra e classifique o desconto por faixas de valor (0%, 5%, 10%, 15%). Dentro da faixa de 15% (valor > R$500), adicione uma checagem aninhada: se o valor for maior que R$1000, o desconto sobe pra 20%.

purchase = float(input("Enter a price: "))

if purchase > 1000:
    discount = 0.20
elif purchase > 500:
    discount = 0.15
elif purchase > 200:
    discount = 0.10
else:
    discount = 0.05

print(f"The discount is: {discount * 100:.0f}%")
print(f"Final price after discount: {purchase - purchase * discount:.2f}")
