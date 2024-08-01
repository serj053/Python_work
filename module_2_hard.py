x = 4
m2 = []
m1 = []
for i in range(1, x):
    for j in range(i, x):
        if x % (i + j) == 0:
            m1 = str(i) + str(j)
            m2.append(m1)

for i in range(1,len(m2)):
    m2[0] += m2[i]

print(m2[0])
