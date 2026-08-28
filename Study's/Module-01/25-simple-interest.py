#Dadas as variáveis principal, rate e time, calcule o juro simples.

principal = float(input("Enter principal amount: "))
rate = float(input("Enter interest rate: "))
time = float(input("Enter time in years: "))

simple_interest = principal * rate * time
print(f"Simple Interest: {simple_interest}")