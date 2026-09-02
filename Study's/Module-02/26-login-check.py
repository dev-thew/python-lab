#Peça usuário e senha, compare com valores fixos no código (ex: usuário esperado "admin", senha esperada "1234"). Informe se o login foi bem-sucedido — só é bem-sucedido se AMBOS estiverem corretos.

user = str(input("Enter a User: "))
password = str(input("Enter a Password: "))

if user == "admin":
    if password == "1234":
        print("Login Successful")
    else:
        print("Login Failed, Try Again")
else:
    print("Login Failed, Try, Again")
