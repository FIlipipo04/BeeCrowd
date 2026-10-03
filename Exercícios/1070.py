x = int(input())
if x % 2 == 0:
    x += 1
    b = x +10
else:
    b = x + 10
for p in range(x, b+1, 2):
    print(p)
