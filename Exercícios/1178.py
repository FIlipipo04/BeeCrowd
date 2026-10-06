lista = []
entrada = float(input())
lista.append(entrada)
for c in range(99):
    entrada = entrada / 2
    lista.append(entrada)
for c in range(100):
    print(f'N[{c}] = {lista[c]:.4f}')