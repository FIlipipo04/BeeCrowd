contador = int(input())
for c in range(0, contador):
    entrada = int(input())
    if entrada == 0:
        print('NULL')
    elif entrada % 2 == 0:
        if entrada < 0:
            print('EVEN NEGATIVE')
        elif entrada > 0:
            print('EVEN POSITIVE')
    elif entrada % 2 != 0:
        if entrada < 0:
            print('ODD NEGATIVE')
        elif entrada > 0:
            print('ODD POSITIVE')