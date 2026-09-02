#Peça o valor da compra e se o cliente é membro do clube de fidelidade (responda "sim" ou "não" como string). O desconto de 15% só se aplica se o valor for maior que R$200 E o cliente for membro.

purchase = float(input("Enter a price: "))
member = str(input("You are Member (yes or no): "))

if member == "yes" and purchase > 200:
    discount = 0.15
    print(f"Discount applied. Final price: {purchase - purchase * discount}.")
else:
    print(f"No discount applied. Final price: {purchase}.")