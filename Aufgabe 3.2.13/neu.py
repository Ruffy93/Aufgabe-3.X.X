BLAU = "\033[94m"
ORANGE = "\033[33m"
ROT = "\033[91m"
RESET = "\033[0m" 

def farbige_ausgabe(temp):
    if temp <= 10:
        return f"{BLAU}{temp:.2f} °C{RESET}"
    elif 11 <= temp <= 20:
        return f"{ORANGE}{temp:.2f} °C{RESET}"
    else:
        return f"{ROT}{temp:.2f} °C{RESET}"

def celsius_zu_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_zu_celsius(f):
    return (f - 32) * 5 / 9

def celsius_zu_kelvin(c):
    return c + 273.15

def kelvin_zu_celsius(k):
    return k - 273.15

def fahrenheit_zu_kelvin(f):
    return (f - 32) * 5 / 9 + 273.15

def kelvin_zu_fahrenheit(k):
    return (k - 273.15) * 9 / 5 + 32

def zeige_menue():
    print("\n" + "=" * 30)
    print(" ❄️ 🥶 Temperaturumrechner 🥵🔥")
    print("=" * 30)
    print("\nUmrechnung wählen:")
    print("1: °C -> °F")
    print("2: °F -> °C")
    print("3: °C -> K")
    print("4: K -> °C")
    print("5: °F -> K")
    print("6: K -> °F")
    print("7: Beenden")
    print("=" * 30)

while True:
    zeige_menue()
    auswahl = input("Ihre Wahl (1–7): ")

    if auswahl == "1":
        c = float(input("°C eingeben: "))
        print(f"{c} °C = {celsius_zu_fahrenheit(c):.2f} °F")

    elif auswahl == "2":
        f = float(input("°F eingeben: "))
        c = fahrenheit_zu_celsius(f)
        print(f"{f} °F = {farbige_ausgabe(c)}")

    elif auswahl == "3":
        c = float(input("°C eingeben: "))
        print(f"{c} °C = {celsius_zu_kelvin(c):.2f} K")

    elif auswahl == "4":
        k = float(input("K eingeben: "))
        c = kelvin_zu_celsius(k)
        print(f"{k} K = {farbige_ausgabe(c)}")

    elif auswahl == "5":
        f = float(input("°F eingeben: "))
        k = fahrenheit_zu_kelvin(f)
        print(f"{f} °F = {k:.2f} K")

    elif auswahl == "6":
        k = float(input("K eingeben: "))
        f = kelvin_zu_fahrenheit(k)
        print(f"{k} K = {f:.2f} °F")

    elif auswahl == "7":
        print("Programm beendet.")
        break

    else:
        print("Ungültige Auswahl.")