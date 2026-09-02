#Peça renda mensal e valor do empréstimo solicitado. Primeiro verifique se a renda é suficiente (renda >= valor / 10); se for, verifique aninhadamente se o cliente já tem outro empréstimo em aberto ("sim"/"não") — se tiver, é preciso aprovação manual; se não tiver, é aprovado automaticamente.

monthly_income = float(input("Enter your monthly income: "))
loan_amount = float(input("Enter the requested loan amount: "))

if monthly_income >= loan_amount / 10:
    has_other_loan = str(input("Do you have another loan in progress (yes or no): "))
    if has_other_loan == "yes":
        print("Manual approval required.")
    else:
        print("Loan approved automatically.")
else:
    print("Income insufficient for the requested loan amount.")