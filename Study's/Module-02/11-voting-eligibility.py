#Peça a idade e informe se a pessoa pode votar (16+), sendo obrigatório dos 18 aos 69, e facultativo entre 16-17 ou 70+. Por enquanto, apenas diferencie "pode votar" (16+) de "não pode votar" (<16) — sem detalhar a obrigatoriedade ainda (isso vem depois com elif).

age = int(input("Enter your age: "))

if age >= 16:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")