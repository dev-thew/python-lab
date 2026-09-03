#Dada a idade (age) e o dia da semana (weekday, como texto, ex: "Wednesday"), calcule o preço do ingresso: R$20 normalmente, com desconto de 50% para menores de 12 ou maiores de 60, e desconto adicional de R$5 se for quarta-feira (os descontos podem se acumular).

age = int(input("Enter your age: "))
week_day = str(input("Enter a Weekday: "))
ticket = 20

if age < 12 or age > 60:
    discount = ticket - ticket * 0.50
    ticket -= discount
    if week_day == "Wednesday":
        discount_additional = 5
        discount -= discount_additional
        ticket -= discount
        print(f"Price the Ticket: {ticket}")
    else:
        print(f"Price The Ticket: {ticket}")
elif week_day == "Wednesday":
    discount_additional = 5
    ticket -= discount_additional
    print(f"Price the Ticket: {ticket}")
else: 
    print(f"Price the Ticket: {ticket}")
    