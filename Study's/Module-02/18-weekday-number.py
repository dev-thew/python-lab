#Peça um número de 1 a 7 e exiba o nome do dia da semana correspondente (1 = Domingo). Se o número for inválido, exiba uma mensagem de erro.

day_number = int(input("Enter a number from 1 to 7: "))

if day_number == 1:
    print("The day of the week is Sunday.")
elif day_number == 2:
    print("The day of the week is Monday.")
elif day_number == 3:
    print("The day of the week is Tuesday.")
elif day_number == 4:
    print("The day of the week is Wednesday.")
elif day_number == 5:
    print("The day of the week is Thursday.")
elif day_number == 6:
    print("The day of the week is Friday.")
elif day_number == 7:
    print("The day of the week is Saturday.")
else:
    print("Error: Invalid number. Please enter a number from 1 to 7.")
