#Peça o saldo de uma conta bancária e informe se está "Positivo" ou "Negativo" (considere zero como "Positivo").

balance = float(input("Enter your bank account balance: "))

if balance >= 0:
    print(f"The account balance is Positive: {balance}.")
else:
    print(f"The account balance is Negative: {balance}.")