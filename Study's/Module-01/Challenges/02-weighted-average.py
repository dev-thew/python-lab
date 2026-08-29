#Dadas três notas e seus respectivos pesos (ex: nota 7 com peso 2, nota 8 com peso 3, nota 9 com peso 5), calcule a média ponderada.
n1 = float(input("Enter the first grade: "))
n2 = float(input("Enter the second grade: "))
n3 = float(input("Enter the third grade: "))

p1 = float(input("Enter the weight for the first grade: "))
p2 = float(input("Enter the weight for the second grade: "))
p3 = float(input("Enter the weight for the third grade: "))

weighted_average = (n1 * p1 + n2 * p2 + n3 * p3) / (p1 + p2 + p3)

print(f"The weighted average is: {weighted_average:.1f}")