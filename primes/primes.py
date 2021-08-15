
num = 50

numbers = []

for x in range(1, num + 1):
    numbers.append(x)

for x in range(2, num):
    for i in range(x + 1, num, x):
        if (numbers[i] > 0 and numbers[i] % x == 0):
            numbers[i] = 0

primes = []

for x in numbers:
    if x != 0:
        primes.append(x)

print(primes)