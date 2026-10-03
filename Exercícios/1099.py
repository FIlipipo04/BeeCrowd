num = int(input())

for c in range(num):
    contador = 0
    x, y = map(int, input().split())
    if x < y:
        for i in range(x + 1, y):
            if i % 2 != 0:
                contador += i
        print(contador)
    elif x == y:
        print(contador)
    elif x > y:
        y, x = x, y
        for i in range(x + 1, y):
            if i % 2 != 0:
                contador += i
        print(contador)
                