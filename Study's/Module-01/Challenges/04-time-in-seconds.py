#Peça ao usuário horas, minutos e segundos (três input() separados) e imprima o total convertido em segundos.

hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))

convertion = hours * 3600
convertion += minutes * 60
convertion += seconds

print(f"Result the convertion for seconds: {convertion}")