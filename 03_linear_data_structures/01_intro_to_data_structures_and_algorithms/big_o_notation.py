# Grafiken zum Code in big_o_notation.excalidraw
values = [3, 1, 4, 1, 5, 9]
n = len(values)
print("Länge der Liste als n:", n)
print("Liste values:", values)
print("Fixe Indexposition:", values[0])

visits = 0
for value in values:
    visits += 1
    # Loop über jeden Wert ist gleich 1 Visit mehr
print("Vists:", visits)

pairs = 0
# Loop in Loop
# für jedes Element gehen wir values nochmal komplett durch
for left in values:
    for right in values:
        pairs += 1
print("Anzahl Paare:", pairs)
