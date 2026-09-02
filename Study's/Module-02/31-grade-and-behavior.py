#Peça a média de um aluno e, dentro da lógica de aprovação, adicione uma verificação extra: se a média for exatamente 6 ou 7 (a chamada "zona de recuperação"), pergunte também o comportamento ("bom"/"ruim") para decidir aprovação — usando if aninhado dentro do elif.

grade = float(input("Enter the student's average grade: "))
if grade >= 7:
    print("Student approved.")
elif grade == 6 or grade == 7:
    behavior = str(input("Enter the student's behavior (good or bad): "))
    if behavior == "good":
        print("Student approved.")
    else:
        print("Student not approved.")