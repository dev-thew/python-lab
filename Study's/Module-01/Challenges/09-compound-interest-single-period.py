#Dado um valor principal (principal), uma taxa de juros (rate) e o número de períodos (periods), calcule o montante final usando juros compostos.

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate (as a percentage): ")) / 100
periods = int(input("Enter the number of periods: "))

final_amount = principal * (1 + rate) ** periods

print(f"Final amount after {periods} periods: {final_amount:.2f}")

