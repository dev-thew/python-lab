#Dado um valor de compra (purchase_value) e um valor pago em dinheiro (amount_paid), calcule e imprima o troco a devolver.

purchase_value = float(input("Enter the purchase value: "))
amount_paid = float(input("Enter the amount paid in cash: "))
change = amount_paid - purchase_value

print(f"The change to be returned is: $ {change:.2f}")