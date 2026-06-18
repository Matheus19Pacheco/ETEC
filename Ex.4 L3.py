n = int(input("Digite a posição desejada: "))

f1 = 1
f2 = 1

if n == 1 or n == 2:
    print(1)
else:
    for i in range(3, n + 1):
        f3 = f1 + f2
        f1 = f2
        f2 = f3

    print(f"O termo é {f3}")
