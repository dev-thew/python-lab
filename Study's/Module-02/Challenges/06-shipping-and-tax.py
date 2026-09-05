#Dado o valor de um produto (product_value) e o estado de destino (state, como texto), calcule o valor final somando frete (grátis acima de R$300, senão R$20) e um imposto extra de 5% apenas se o estado for "SP".

product_value = float(input("Enter the product value (R$): "))
state = input("Enter the destination state: ")

shipping_cost = 0

if product_value <= 300:
    shipping_cost = 20

tax = 0
if state == "SP":
    tax = product_value * 0.05

final_value = product_value + shipping_cost + tax

print(f"Final value: R${final_value:.2f}")