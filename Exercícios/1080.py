maior = 0
pos = 0

for c in range(1, 101):
    num = int(input())
    if num > maior:
        maior = num
        pos = c

print(maior)
print(pos)
