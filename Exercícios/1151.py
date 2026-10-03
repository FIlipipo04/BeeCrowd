a = 0
b = 1

entrada = int(input())

lista = []

for _ in range(entrada):
    lista.append(a)
    a, b = b, a+b

print(*lista, sep=' ')