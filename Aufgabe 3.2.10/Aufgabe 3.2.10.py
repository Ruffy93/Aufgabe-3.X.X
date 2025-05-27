summe = 0

for zahl in range(1, 101):
    if zahl % 2 == 0:
        summe += zahl

print("Die Summe aller geraden Zahlen von 1 bis 100 ist:", summe)

grenze = int(input("Bis zu welcher Zahl sollen die geraden Zahlen summiert werden? "))

summe = 0

for zahl in range(1, grenze + 1):
    if zahl % 2 == 0:
        summe += zahl

print(f"Summe aller geraden Zahlen von 1 bis {grenze} ist: {summe}")