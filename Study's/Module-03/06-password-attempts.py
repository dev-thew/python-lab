#Defina uma variável correct_password com um valor fixo no código (ex.: "python123"). Peça ao usuário uma senha repetidamente usando while, até que ele acerte. Exiba "Acesso liberado!" quando a senha correta for digitada.

correct_password = "python123"
password = ""

while password != correct_password:
    password = str(input("Enter a Password: "))

print("Full Acess!")