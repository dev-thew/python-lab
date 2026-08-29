#Peça ao usuário um valor em reais (como texto) e uma cotação do dólar (como texto), converta ambos para float, e imprima o valor convertido em dólares, arredondado para 2 casas decimais.

real_value = float(input("Enter the amount in Brazilian Reais (R$): "))
dollar_exchange_rate = float(input("Enter the current exchange rate (R$/USD): "))
dollar_value = real_value / dollar_exchange_rate

print(f"The equivalent amount in US Dollars is: $ {dollar_value:.2f}")