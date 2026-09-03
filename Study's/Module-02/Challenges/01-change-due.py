#Dado um valor de compra (purchase_value) e um valor pago em dinheiro (amount_paid), calcule e imprima o troco a devolver.

purchase_value = float(input("Enter the purchase value: "))
amount_paid = float(input("Enter the amount paid in cash: "))

change = amount_paid - purchase_value

if change < 0:
    print("Insufficient funds.")
else:
    print(f"Change to be returned: ${change:.2f}")