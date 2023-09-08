# задача 9
# Данил Шамардин
# 02.09.2023
a = 2
b = 1
c = a
for i in range(2, 6):
    for j in range(b, a):
        c -= 1
        print(c, end=" ")
    print(" ")
    b = a
    a += i
    c = a