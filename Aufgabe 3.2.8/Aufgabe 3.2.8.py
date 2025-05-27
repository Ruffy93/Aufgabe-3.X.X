zahlenn = [4, 7, 2, 9, 1, 5, 3, 23, 14, 324, 423, 4645, 6785]

print("Länge:", len(zahlenn))
print("Größe:", max(zahlenn))
print("Kleinste Zahl:", min(zahlenn))

mittelwert = sum(zahlenn) / len(zahlenn)
print("Mittelwert:", mittelwert)
print("umgekehrt:", list(reversed(zahlenn)))

gerade_zahlen = [zahl for zahl in zahlenn if zahl % 2 == 0]
print("Gerade Zahlen:", gerade_zahlen)