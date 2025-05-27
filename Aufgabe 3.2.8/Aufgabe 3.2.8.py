zahlen = [4, 7, 2, 9, 1, 5, 3, 23, 14, 324, 423, 4645, 6785]

print("Länge:", len(zahlen))
print("Größe:", max(zahlen))
print("Kleinste Zahl:", min(zahlen))

mittelwert = sum(zahlen) / len(zahlen)
print("Mittelwert:", mittelwert)
print("umgekehrt:", list(reversed(zahlen)))

gerade_zahlen = [zahl for zahl in zahlen if zahl % 2 == 0]
print("Gerade Zahlen:", gerade_zahlen)