#Dado o valor total do carrinho (cart_total), se o cliente é membro (is_member, "sim"/"não") e a forma de pagamento (payment_method, "pix" ou "cartão"), calcule o valor final aplicando em sequência: desconto de 10% para membros com carrinho acima de R$150, e desconto adicional de 5% para pagamento via Pix — mas o desconto do Pix só se aplica se o valor já tiver algum desconto de membro aplicado.

cart_total = float(input("Enter the total cart value (R$): "))
is_member = input("Is the customer a member? (yes/no): ")
payment_method = input("Enter the payment method (pix/card): ")

if is_member == "yes" and cart_total > 150:
    discounted_total = cart_total * 0.9  # Apply 10% discount
    if payment_method == "pix":
        final_total = discounted_total * 0.95  # Apply additional 5% discount for Pix
    else:
        final_total = discounted_total
else:
    final_total = cart_total

print(f"Final total: R${final_total:.2f}")