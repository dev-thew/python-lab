#Combine os dois exercícios anteriores de triângulo: primeiro verifique (com if aninhado) se os lados formam um triângulo válido; só se for válido, classifique em Equilátero/Isósceles/Escaleno.

side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    if side1 == side2 == side3:
        print("The triangle is Equilateral.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("The sides do not form a valid triangle.")
    