#Dados peso (weight), altura (height) e idade (age), calcule o IMC e gere um relatório combinando a classificação do IMC com a faixa etária da pessoa em uma única frase.

weight = float(input("Enter a weight: "))
height = float(input("Enter a height: "))
age = int(input("Enter your age: "))

bmi = weight / height ** 2

if age < 5:
    print("Age is too low to calculate BMI.")
else:
    if age >= 18:
        age_group = "adult"
    elif age >= 15:
        age_group = "teenager"
    else:
        age_group = "child"

    if bmi < 18.5:
        bmi_group = "underweight"
    elif bmi < 25:
        bmi_group = "normal weight"
    elif bmi < 30:
        bmi_group = "overweight"
    else:
        bmi_group = "obese"

    print(f"Your BMI is {bmi:.2f}, you are {bmi_group} and you are a {age_group}.")
