#Peça peso (kg) e altura (m) ao usuário, calcule o IMC, e imprima o resultado arredondado para 1 casa decimal.

weight = float(input("Enter your weight in kg: ")) 
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)
print(f"Your BMI is: {round(bmi, 1)}")