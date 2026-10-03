num = 7
for i in range(1, 10, 2):
    for j in range(num, num-3, -1):
        print(f'I={i} J={j}')
    num += 2