son = int(input("Uch xonali son kiriting: "))

birlik = son % 10
onlik = (son // 10) % 10
yuzlik = son // 100

teskari = birlik * 100 + onlik * 10 + yuzlik
print("Teskari son:", teskari)
