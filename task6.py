# задача 6
# Данил Шамардин
# 02.09.2023
for i in range(1, 6):
    for j in range(i, -i, -1):
        if j > 0:
            print(j, end = " ")
    print(" ")