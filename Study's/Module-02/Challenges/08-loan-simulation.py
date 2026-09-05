#Dados renda mensal (monthly_income), valor solicitado (loan_amount) e se o cliente é "novo" ou "antigo" (client_type), decida a aprovação: clientes antigos precisam de renda >= valor/15; clientes novos precisam de renda >= valor/8 (critério mais rigoroso).

monthly_income = float(input("Enter the monthly income (R$): "))
loan_amount = float(input("Enter the requested loan amount (R$): "))
client_type = input("Enter the client type (new/old): ")

if client_type == "old":
    if monthly_income >= loan_amount / 15:
        approval = "approved"
    else:
        approval = "denied"
elif client_type == "new":
    if monthly_income >= loan_amount / 8:
        approval = "approved"
    else:
        approval = "denied"

print(f"The loan request is {approval}.")