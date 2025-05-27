zahlen = []

while True:
    eingabe = input("Bitte eine Zahl eingeben (oder 'stop' zum Beenden): ")
    
    if eingabe.lower() == "stop":
        break

    try:
        zahl = int(eingabe)
        zahlen.append(zahl)
    except ValueError:
        print("Ungültige Eingabe! Bitte eine ganze Zahl eingeben.")
        
if not zahlen:
    print("Es wurden keine gültigen Zahlen eingegeben.")
else:
    minimum = zahlen[0]
    maximum = zahlen[0]
    summe = 0

    for zahl in zahlen:
        if zahl < minimum:
            minimum = zahl
        if zahl > maximum:
            maximum = zahl
        summe += zahl

    durchschnitt = round(summe / len(zahlen), 2)

    sortierte_zahlen = sorted(zahlen)

    print("\n--- Analyse ---")
    print("Eingegebene Zahlen:", zahlen)
    print("Sortiert (aufsteigend):", sortierte_zahlen)
    print("Kleinste Zahl:", minimum)
    print("Größte Zahl:", maximum)
    print("Durchschnitt:", durchschnitt)