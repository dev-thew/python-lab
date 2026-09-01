#Peça a idade e classifique em: Criança (0–11), Adolescente (12–17), Adulto (18–59), Idoso (60+).

age = int(input("Enter your age: "))

if 0 <= age <= 11:
    print(f"You are {age} years old.\nClassification: Child.")
elif 12 <= age <= 17:
    print(f"You are {age} years old.\nClassification: Teenager.")
elif 18 <= age <= 59:
    print(f"You are {age} years old.\nClassification: Adult.")
else:
    print(f"You are {age} years old.\nClassification: Senior.")
