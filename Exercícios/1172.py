lista = []
for c in range(10):
    entrada = int(input())
    lista.append(entrada)
    if lista[c] < 1:
        lista[c] = 1
    print(f'X[{c}] = {lista[c]}')
    