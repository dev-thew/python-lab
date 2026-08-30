#Peça ao usuário três números (via input(), convertidos para float) e imprima três booleanos: se o primeiro é maior que o segundo, se o segundo é maior que o terceiro, e se os três são diferentes entre si (usando and).
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

is_first_greater = n1 > n2
is_second_greater = n2 > n3
are_all_different = n1 != n2 and n2 != n3 and n1 != n3

print(f"Is the first number greater than the second? {is_first_greater}")
print(f"Is the second number greater than the third? {is_second_greater}")
print(f"Are all three numbers different? {are_all_different}")