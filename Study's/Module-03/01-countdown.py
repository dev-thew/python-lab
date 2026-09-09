#Peça ao usuário um número inteiro start e exiba uma contagem regressiva de start até 1, um número por linha, usando while.

start = int(input("Enter a Number: "))

while start > 0:
    print(start)
    start -= 1