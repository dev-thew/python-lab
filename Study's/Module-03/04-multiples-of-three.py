#Peça ao usuário um número inteiro limit e exiba todos os múltiplos de 3 entre 1 e limit (inclusive), usando while.

limit = int(input("Enter a Limit: "))
num = 1

while num <= limit:
    if num % 3 == 0:
     print(num)
    num += 1