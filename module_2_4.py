numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print(numbers[::])
primes = []
not_primes = []
for k in range(len(numbers)):
    if k == 0 or k == 1:
        continue
    n = 0
    nn = len(numbers[0:k])
    for j in range(nn):
        if numbers[k-1] % (j + 1) == 0:
            n += 1
    if n == 2:
        primes.append(k)
    else:
        not_primes.append(k)

print(primes)
print(not_primes)
