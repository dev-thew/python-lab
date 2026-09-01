#Peça a idade e informe se o ingresso é "Meia-entrada" (menor de 12 ou 60+) ou "Inteira".

age = int(input("Enter your age: "))

if age < 12:
    print("The ticket price is 'Meia-entrada' (half-price).")
else:
    if age >= 60:
        print("The ticket price is 'Meia-entrada' (half-price).")
    else:
        print("The ticket price is 'Inteira' (full-price).")

