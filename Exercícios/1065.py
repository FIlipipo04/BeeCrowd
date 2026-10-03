contador = 0
for c in range(0, 5):
    entrada = int(input())
    if entrada % 2 == 0:
        contador += 1
print(f'{contador} valores pares')