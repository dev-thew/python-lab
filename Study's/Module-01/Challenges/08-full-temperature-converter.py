#Peça ao usuário uma temperatura em Fahrenheit e converta para Celsius e para Kelvin, imprimindo os dois resultados.

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9
kelvin = celsius + 273.15

print(f"Temperature in Celsius: {celsius:.2f} °C")
print(f"Temperature in Kelvin: {kelvin:.2f} K")