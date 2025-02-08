K = 8
hafta_kuni = (K % 7) + (K % 7 == 0) * 7  # 0 bo'lsa, 7 ga o'zgartiramiz
print(hafta_kuni)  # 1 (Dushanba)
