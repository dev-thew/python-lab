#Dado um valor de compra (purchase_value), calcule o valor com 15% de desconto aplicado, e imprima tanto o valor do desconto quanto o valor final — sem usar if para checar faixas, é sempre 15% fixo.

purchase_value = float(input("Enter with a value: "))
discount = (purchase_value) * 0.15
total = purchase_value - discount

print(f"Discount: {discount}")
print(f"Total: {total}")
