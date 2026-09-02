#Peça um ano e informe se é bissexto. Regra: divisível por 4 E (não divisível por 100 OU divisível por 400).
#dica: combine and/or numa única condição

year = int(input("Enter a year:"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(f"Year: {year}\nIt is a leap year")
else:
    print(f"Year: {year}\nIt is not a leap year")
