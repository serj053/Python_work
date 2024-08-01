x = 20
m4 = []  #для представления в виде пар чисел
m3 = []  #для представления в виде пар чисел
m2 = []  #для представления в виде строки
m1 = []  #для представления в виде строки
for i in range(1, x):
    for j in range(i, x):
        if x % (i + j) == 0:
            m1 = str(i) + str(j)
            m3 = [i, j]
            m2.append(m1)
            m4.append(m3)

print(m4)

for i in range(1, len(m2)):
    m2[0] += m2[i]

print(m2[0])
