#Peça dois números e informe qual é o maior. Considere o caso de serem iguais também.

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

if number1 > number2:
    print(f"The first number {number1} is greater than the second number {number2}.")

if number2 > number1:
    print(f"The second number {number2} is greater than the first number {number1}.")

if number1 == number2:
    print(f"Both numbers are equal: {number1} = {number2}.")