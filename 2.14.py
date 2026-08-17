temperaturas = [22.5, 23.0, 21.0, 19.5, 25.0, 26.5, 24.0]

maxtemp = 0
media = 0
mintemp = temperaturas[0]

for indice in temperaturas:
    if maxtemp < indice:
        maxtemp = indice

    if mintemp > indice:
        mintemp = indice

    media = media + indice

media = media / len(temperaturas)

print("Máximo: " , maxtemp)
print("Media: " , media)
print("Mínimo: " , mintemp)