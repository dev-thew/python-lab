#Peça uma hora (0–23) e informe o período do dia: Madrugada (0–5), Manhã (6–11), Tarde (12–17), Noite (18–23).

hour = int(input("Enter an hour (0-23):"))

if 0 <= hour <= 5:
    print(f"Hour: {hour}\nPeriod: Early Morning")
elif 6 <= hour <= 11:
    print(f"Hour: {hour}\nPeriod: Morning")
elif 12 <= hour <= 17:
    print(f"Hour: {hour}\nPeriod: Afternoon")
else:
    print(f"Hour: {hour}\nPeriod: Night")
