num = int(input())
total_coelho = 0
total_ratos = 0
total_sapos = 0
total_cobaias = 0

for _ in range(num):
    qtd, tipo = input().split()
    tipo = tipo.upper()
    qtd = int(qtd)
    if tipo == 'C':
        total_coelho += qtd
    elif tipo == 'R':
        total_ratos += qtd
    elif tipo == 'S':
        total_sapos += qtd
total_cobaias = total_ratos + total_coelho + total_sapos

print(f'Total: {total_cobaias} cobaias')
print(f'Total de coelhos: {total_coelho}')
print(f'Total de ratos: {total_ratos}')
print(f'Total de sapos: {total_sapos}')
print(f'Percentual de coelhos: {total_coelho/total_cobaias * 100:.2f} %')
print(f'Percentual de ratos: {total_ratos/total_cobaias * 100:.2f} %')
print(f'Percentual de sapos: {total_sapos/total_cobaias * 100:.2f} %')
