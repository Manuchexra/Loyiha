asosiy_omonat = float(input("Omonat miqdorini kiriting: "))
foiz = float(input("Yillik foiz stavkasini kiriting: "))
yillar = int(input("Necha yil davomida saqlamoqchisiz: "))
oxirgi_summ = asosiy_omonat * (1 + foiz / 100) ** yillar
print(f"{yillar} yil oxirida to‘plangan summa: {oxirgi_summ}")
