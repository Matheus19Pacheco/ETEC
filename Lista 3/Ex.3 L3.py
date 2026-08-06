paisA = 80000
paisB = 200000
anos = 0

while paisA < paisB:
    paisA = paisA + (paisA * 0.03)
    paisB = paisB + (paisB * 0.015)
    anos += 1

print(f"Serão necessários {anos} anos.")
