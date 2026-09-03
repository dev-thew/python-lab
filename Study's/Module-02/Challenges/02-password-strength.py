#Dada uma senha (password), classifique sua força: "Fraca" (menos de 6 caracteres), "Média" (entre 6 e 10 caracteres), "Forte" (mais de 10 caracteres). Se a senha tiver menos de 4 caracteres, ignore as outras faixas e classifique direto como "Muito fraca".

password = input("Enter a password: ")

if len(password) < 6:
    if len(password) < 4:
        print(f"This Password is a Very Weak")
    else:
        print(f"This Password is a Weak")
elif len(password) >= 6 and len(password) <= 10:
    print(f"This Password is a Medium")
elif len(password) > 10: 
    print(f"This Password is a Stronger")
else:
    print("Insert a Password")

