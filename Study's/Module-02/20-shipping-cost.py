#Peça o peso de um pacote (kg) e calcule o frete: até 1kg = R$10, até 5kg = R$25, até 10kg = R$45, acima de 10kg = R$70.

weight = float(input("Enter the package weight (kg): "))

if weight <= 1:
    shipping_cost = 10
elif weight <= 5:
    shipping_cost = 25
elif weight <= 10:
    shipping_cost = 45
else:
    shipping_cost = 70

print(f"The shipping cost is R${shipping_cost:.2f}.")