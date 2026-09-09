#Peça ao usuário quantos números ele quer somar (amount). Em seguida, peça cada número em um loop while e acumule a soma em total. Exiba o total ao final.

amount = int(input("How many numbers do you want a sum? "))
total = 0
i = 1

while amount >= i:
    num = int(input(f"Enter a Number {i}: "))
    i += 1
    total += num

print(f"Total: {total}")

