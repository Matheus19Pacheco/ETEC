import random

v1 = []
v2 = []
v3 = []

i = 0

while i < 10:

    v1.append(random.randint(1, 100))
    v2.append(random.randint(1, 100))

    i = i + 1

i = 0

while i < 10:

    v3.append(v1[i])
    v3.append(v2[i])

    i = i + 1

print("Vetor 1:", v1)
print("Vetor 2:", v2)
print("Vetor 3:", v3)
