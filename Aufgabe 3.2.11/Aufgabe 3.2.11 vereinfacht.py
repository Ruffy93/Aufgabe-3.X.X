zahlen = []

while True:
    eingabe = input("Zahl eingeben (oder 'stop'): ")

    if eingabe.lower() == "stop":
        break

    if eingabe.isdigit() or (eingabe.startswith('-') and eingabe[1:].isdigit()):
        zahlen.append(int(eingabe))
    else:
        print("Bitte nur ganze Zahlen eingeben!")

if zahlen:
    print("\n--- Analyse ---")
    print("Eingegebene Zahlen:  ", zahlen)
    print("Sortiert:            ", sorted(zahlen))
    print("Kleinste Zahl:       ", min(zahlen))
    print("Größte Zahl:         ", max(zahlen))
    print("Durchschnitt:        ", round(sum(zahlen) / len(zahlen), 2))
else:
    print("Keine gültigen Zahlen eingegeben.")