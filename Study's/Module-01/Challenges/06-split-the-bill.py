#Dado o valor total de uma conta (total_bill) e o número de pessoas (number_of_people), calcule quanto cada pessoa deve pagar, incluindo 10% de gorjeta no valor total antes de dividir.

total_bill = float(input("Enter the total bill amount: "))
number_of_people = int(input("Enter the number of people: "))

tip = total_bill * 0.10
total = total_bill + tip
amount_per_person = total / number_of_people

print(f"Total bill with tip: {total:.2f}")
print(f"Amount per person: {amount_per_person:.2f}")
