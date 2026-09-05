#Dados três lados (side_a, side_b, side_c), verifique primeiro se formam um triângulo válido; se formarem, classifique o tipo (Equilátero, Isósceles ou Escaleno); se não formarem, informe qual combinação de lados violou a regra do triângulo.

side_a = float(input("Enter the length of side A: "))
side_b = float(input("Enter the length of side B: "))
side_c = float(input("Enter the length of side C: "))

if (side_a + side_b > side_c) and (side_a + side_c > side_b) and (side_b + side_c > side_a):
    if side_a == side_b == side_c:
        triangle_type = "Equilateral"
    elif side_a == side_b or side_a == side_c or side_b == side_c:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Scalene"
    print(f"The triangle is valid and it is {triangle_type}.")
else:
    if side_a + side_b <= side_c:
        print("Invalid: side_a + side_b does not exceed side_c.")
    elif side_a + side_c <= side_b:
        print("Invalid: side_a + side_c does not exceed side_b.")
    else:
        print("Invalid: side_b + side_c does not exceed side_a.")