#Peça os três lados de um triângulo e classifique: Equilátero (todos iguais), Isósceles (dois iguais), Escaleno (todos diferentes). Não se preocupe em validar se os lados formam um triângulo válido.

side1 = float(input("Enter a side 1:"))
side2 = float(input("Enter a side 2:"))
side3 = float(input("Enter a side 3:"))

if side1 == side2:
    if side2 == side3:
        print(f"Sides: {side1, side2, side3}\nEquilateral")
    else:
        print(f"Sides: {side1, side2, side3}\nIsosceles")
else:
    if side1 == side3:
        print(f"Sides: {side1, side2, side3}\nIsosceles")
    else:
        if side2 == side3:
            print(f"Sides: {side1, side2, side3}\nIsosceles")
        else:
            print(f"Sides: {side1, side2, side3}\nScalene")
            