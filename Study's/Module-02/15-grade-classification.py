#Peça a nota de um aluno (0 a 10) e classifique em conceito: A (>=9), B (>=7), C (>=5), D (<5).

grade = float(input("Enter the student's grade (0 to 10): "))

if grade >= 9:
    print(f"The student's grade is A: {grade}.")
elif grade >= 7:
    print(f"The student's grade is B: {grade}.")
elif grade >= 5:
    print(f"The student's grade is C: {grade}.")
else:
    print(f"The student's grade is D: {grade}.")