soat = int(input("Hozirgi soatni kiriting (0-23 oralig'ida): "))
qoshish = int(input("Nechta soat qo‘shilsin: "))

yangi_soat = (soat + qoshish) % 24
print("Yangi soat:", yangi_soat)
