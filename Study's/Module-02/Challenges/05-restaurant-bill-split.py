#Dado o valor total da conta (total_bill), o número de pessoas (num_people) e se o serviço foi "bom" ou "ruim" (service_quality), calcule o valor por pessoa incluindo 10% de gorjeta se o serviço foi bom, ou sem gorjeta se foi ruim.

total_bill = float(input("Enter the total bill amount: "))
num_people = int(input("Enter the number of people: "))
service_quality = input("Enter the service quality (good/bad): ")

total = total_bill // num_people

if service_quality == "good":
    tip = 0.10
    total += total * tip
    print(f"Value for Person: ${total}")
else:
    print(f"Value for Person: ${total}")
