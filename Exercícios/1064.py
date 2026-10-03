contador = 0
num = 0
soma = 0
for c in range (6):
    num = float(input())
    if num > 0:
        contador += 1
        soma += num
print(f'{contador} valores positivos')
print(f'{soma/contador:.1f}')