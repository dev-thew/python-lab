#Peça o salário e calcule a alíquota de imposto: até 2000 = isento, até 4000 = 10%, até 8000 = 20%, acima de 8000 = 27%.

salary = float(input("Enter your salary:"))

impost_rate = 0

if salary <= 2000:
    impost_rate = 0
elif salary <= 4000:
    impost_rate = 0.10
elif salary <= 8000:
    impost_rate = 0.20
else:
    impost_rate = 0.27

print(f"Tax bracket: {impost_rate * 100:.0f}%")