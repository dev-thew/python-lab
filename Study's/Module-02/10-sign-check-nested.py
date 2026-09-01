#Peça um número e informe se ele é positivo, negativo ou zero — usando if/else aninhado (sem elif ainda, só pra comparar com a versão que vem depois).

number = float(input("Enter a number: "))

if number > 0:
    print(f"The number {number} is positive.")
else:
    if number < 0:
        print(f"The number {number} is negative.")
    else:
        print(f"The number is zero.")