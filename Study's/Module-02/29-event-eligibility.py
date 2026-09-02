#Peça a idade e se a pessoa está acompanhada de um responsável ("sim"/"não"). A entrada é permitida se a idade for >= 18, OU se for menor de 18 mas estiver acompanhada.

age = int(input("Enter your age: "))
accompanied = str(input("Are you accompanied by a responsible adult (yes or no): "))

if age >= 18 or (age < 18 and accompanied == "yes"):
    print("Entry allowed.")
else:
    print("Entry not allowed.")