positivo = 0
negativo = 0
par = 0
impar = 0
for c in range(0, 5):
    entrada = int(input())
    if entrada % 2 == 0:
        par += 1
    if entrada % 2 != 0:
        impar += 1

    if entrada > 0:
        positivo += 1
    if entrada < 0:
        negativo += 1


print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')