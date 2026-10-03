x = int(input())
y = int(input())
soma = 0

for p in range(y+1, x):
    if p % 2 != 0:
        soma = soma + p
print(soma)
