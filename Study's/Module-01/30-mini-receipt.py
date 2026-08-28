#Dadas as variáveis item_name, item_price e quantity, imprima um pequeno recibo formatado mostrando o item, quantidade, preço unitário e total (preço × quantidade), usando f-string.

item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total = item_price * quantity

print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"Unit Price: ${item_price:.2f}")
print(f"Total: ${total:.2f}")
