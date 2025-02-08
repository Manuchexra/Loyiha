sekund = int(input("Sekundni kiriting: "))

kun = sekund // (24 * 3600)
sekund = sekund % (24 * 3600)

soat = sekund // 3600
sekund = sekund % 3600

minut = sekund // 60
sekund = sekund % 60

print(f"{kun} kun, {soat} soat, {minut} minut, {sekund} sekund")
