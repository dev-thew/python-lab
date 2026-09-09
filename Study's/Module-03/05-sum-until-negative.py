#Peça ao usuário números inteiros repetidamente, um por vez, e some todos eles em uma variável total. O loop deve parar assim que o usuário digitar um número negativo. Ao final, exiba o total (sem contar o número negativo).

num = int(input("Enter a Number: "))
total = 0

while num >= 0:
    total += num
    num += 1
    num = int(input("Enter a Number: "))

print(f"Total = {total}")