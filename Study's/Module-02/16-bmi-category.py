#Peça peso (kg) e altura (m), calcule o IMC (peso / altura ** 2) e classifique: Abaixo do peso (<18.5), Normal (18.5–24.9), Sobrepeso (25–29.9), Obesidade (>=30).

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

BMI = weight / (height ** 2)

if BMI < 18.5:
    print(f"Your BMI is {BMI:.2f}.\nClassification: Underweight.")
elif 18.5 <= BMI < 25:
    print(f"Your BMI is {BMI:.2f}.\nClassification: Normal weight.")
elif 25 <= BMI < 30:
    print(f"Your BMI is {BMI:.2f}.\nClassification: Overweight.")
else:
    print(f"Your BMI is {BMI:.2f}.\nClassification: Obesity.")