entrada = int(input())

for _ in range(entrada):
    num = int(input())
    contador = 0
    for c in range(1, num+1):
        if num % c == 0:
            contador += 1
    if contador == 2:
        print(f'{num} eh primo')
    else:
        print(f'{num} nao eh primo')