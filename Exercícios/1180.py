entrada = int(input())
aux = list(map(int, input().split()))
menor = aux[0]
pos = 0
for c in range(entrada):
    if menor > aux[c]:
        menor = aux[c]
        pos = c
print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')