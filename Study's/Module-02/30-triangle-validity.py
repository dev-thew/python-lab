#Peça os três lados de um triângulo e informe se eles formam um triângulo válido. Regra: a soma de quaisquer dois lados deve ser maior que o terceiro (as três condições precisam ser verdadeiras ao mesmo tempo).

side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1):
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")