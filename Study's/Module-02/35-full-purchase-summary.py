#Exercício final do módulo, combinando tudo: peça o valor da compra, se o cliente é membro ("sim"/"não") e a forma de pagamento ("pix" ou "cartão"). Aplique nessa ordem: desconto de membro (10%, aninhado dentro da checagem de valor > R$100), depois desconto extra de pagamento à vista via Pix (mais 5% sobre o valor já com desconto). Exiba o valor final.

purchase = float(input("Enter the purchase amount: "))
member = str(input("Are you a member (yes or no): "))
payment_method = str(input("Enter the payment method (pix or card): "))

if purchase > 100:
    if member == "yes":
        purchase -= purchase * 0.10
        if payment_method == "pix":
            purchase -= purchase * 0.05
        print(f"Final price: R${purchase:.2f}")
    else:
        print(f"Final price: R${purchase:.2f}")
else:
    print(f"Final price: R${purchase:.2f}")