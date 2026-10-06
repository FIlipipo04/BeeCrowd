lista = []
for c in range(20):
    lista.append(int(input()))
for c in range(10):
    aux = lista[c]
    lista[c] = lista[19 - c]
    lista[19 - c] = aux
for c in range(20):
    print(f'N[{c}] = {lista[c]}')

# lista = []
# for c in range(20):
#     lista.append(int(input()))
# lista = lista[::-1]
# for c in range(20):
#     print(f'N[{c}] = {lista[c]}')
# eu fiz assim, mas como usa fatiamento e a gente so estudou fatiamento no final do periodo eu tentei fazer da forma mais simples possivel