#Peça ao usuário um número inteiro limit e exiba todos os números pares de 0 até limit (inclusive), usando while.

limit = int(input("Enter a Limit: "))
num = 0

while num <= limit:
    if num % 2 == 0:
     print(num)
    num += 1
    