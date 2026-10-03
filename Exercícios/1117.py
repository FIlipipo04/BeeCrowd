contador = 0
notas = []

while contador < 2:
    entrada = float(input())
    if 0 <= entrada <= 10:
        contador += 1
        notas.append(entrada)
    else:
        print('nota invalida')

print(f'media = {(notas[0] + notas[1])/2}')