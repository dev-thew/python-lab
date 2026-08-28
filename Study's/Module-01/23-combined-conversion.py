#Peça ao usuário dois números como texto, converta os dois para float, e imprima a soma, a diferença e o produto deles.

number1 = input("Enter Number 1: ")
number2 = input("Enter Number 2: ")

number1 = float(number1)
number2 = float(number2)

sum = number1 + number2
sub = number1 - number2
product = number1 * number2

print(f"Sum: {sum}\nSub: {sub}\nProduct: {product}")