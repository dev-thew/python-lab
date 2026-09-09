#Peça ao usuário um número inteiro limit e exiba uma contagem crescente de 1 até limit, um número por linha, usando while.

limit = int(input("Enter a Limit: "))
num = 1

while num <= limit:
    print(num)
    num += 1

