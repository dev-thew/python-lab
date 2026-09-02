#Peça um número e informe se ele está entre 10 e 20 (inclusive) usando uma única condição com and.

number = int(input("Enter a Number: "))

if number >= 10 and number <= 20:
    print(f"Number: {number}\nIs within the range")
else: 
    print(f"Number: {number}\nis not within the range")