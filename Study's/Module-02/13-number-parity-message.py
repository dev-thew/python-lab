#Peça um número inteiro e exiba uma frase completa dizendo se ele é par ou ímpar, incluindo o próprio número na mensagem (use f-string).

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")