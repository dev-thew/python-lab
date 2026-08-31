#Peça uma senha (como texto) e avise se ela tem pelo menos 8 caracteres. Use len() para descobrir o tamanho da string.

password = str(input("Enter a Password (minimun 8 characters): "))

if len(password) < 8:
    print("Password too short")