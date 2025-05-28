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
        print(f"{f} °F = {fahrenheit_zu_celsius(f):.2f} °C")

    elif auswahl == "3":
        c = float(input("°C eingeben: "))
        print(f"{c} °C = {celsius_zu_kelvin(c):.2f} K")

    elif auswahl == "4":
        k = float(input("K eingeben: "))
        print(f"{k} K = {kelvin_zu_celsius(k):.2f} °C")

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
