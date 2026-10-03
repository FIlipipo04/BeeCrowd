cod, qtd = map(int, input().split())
if cod == 1:
    print(f'Total: R$ {qtd * 4:.2f}')
elif cod == 2:
    print(f'Total: R$ {qtd * float(4.5):.2f}')
elif cod == 3:
    print(f'Total: R$ {qtd * 5:.2f}')
elif cod == 4:
    print(f'Total: R$ {qtd * 2:.2f}')
elif qtd == 5:
    print(f'Total: R$ {qtd * float(1.5):.2f}')