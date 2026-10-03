num = int(input())

for _ in range(num):
    entrada = bin(int(input()))
    contador = 0
    for c in entrada:
        if c == '1':
            contador += 1
    print(contador)
#é importante daber que o bin vai retonar uma string, por isso o if tem que comparar com '1'
