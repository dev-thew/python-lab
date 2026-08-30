#Peça ao usuário o nome de um produto, a quantidade vendida e o preço unitário (três input()). Calcule o valor total da venda, aplique 8% de imposto sobre esse total, e imprima um mini relatório com: nome do produto, quantidade, preço unitário, subtotal, valor do imposto e total com imposto — tudo usando f-strings, cada informação em uma linha.

product_name = input("Enter the product name: ")
quantity_sold = int(input("Enter the quantity sold: "))
unit_price = float(input("Enter the unit price: "))

subtotal = quantity_sold * unit_price
tax = subtotal * 0.08
total_with_tax = subtotal + tax

print(f"Product Name: {product_name}")
print(f"Quantity Sold: {quantity_sold}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Tax (8%): ${tax:.2f}")
print(f"Total with Tax: ${total_with_tax:.2f}")

