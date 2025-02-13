a = float(input("1-sonni kiriting: "))
b = float(input("2-sonni kiriting: "))
c = float(input("3-sonni kiriting: "))

qoldiq1 = a % 1
qoldiq2 = b % 1
qoldiq3 = c % 1

jami_qoldiq = qoldiq1 + qoldiq2 + qoldiq3

print("Qoldiqlar yig'indisi:", round(jami_qoldiq, 2))
