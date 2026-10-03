c1, n1, p1 = input().split()
c2, n2, p2 = input().split()

print(f'VALOR A PAGAR: R$ {(int(n1) * float(p1)) + (int(n2) * float(p2)):.2f}')
