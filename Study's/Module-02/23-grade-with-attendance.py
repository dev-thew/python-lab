#Peça a média final e a frequência (%). Se a frequência for menor que 75, o aluno está reprovado por falta, independente da nota. Caso contrário, aplique a mesma lógica de aprovação por nota (>= 6 aprovado).

final_grade = float(input("Enter the final grade:"))
attendance = float(input("Enter the attendance percentage:"))

if attendance < 75:
    print(f"Attendance: {attendance}%\nFailed due to attendance")
else:
    if final_grade >= 6:
        print(f"Final grade: {final_grade}\nAttendance: {attendance}%\nPassed")
    else:
        print(f"Final grade: {final_grade}\nAttendance: {attendance}%\nFailed due to grade")