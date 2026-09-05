#Dadas três notas (grade1, grade2, grade3) e a frequência (attendance), calcule a média das notas, aplique a regra de reprovação por falta (frequência < 75%) com prioridade sobre a nota, e classifique o resultado final em conceito (A/B/C/D) apenas se aprovado.

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the second grade: "))
grade3 = float(input("Enter the third grade: "))
attendance = float(input("Enter the attendance percentage: "))

average_grade = (grade1 + grade2 + grade3) / 3

if attendance < 75:
    result = "Failed due to attendance"
    print(result)
else:
    if average_grade >= 90:
        result = "A"
    elif average_grade >= 80:
        result = "B"
    elif average_grade >= 50:
        result = "C"
    else:
        result = "D"

print(f"Average grade: {average_grade:.2f}")
print(f"Final result: {result}")
