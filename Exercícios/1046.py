inicio, fim = map(int, input().split())
if fim > inicio:
    tempo = fim - inicio
else:
    tempo = 24 - inicio + fim

if inicio == fim:
    tempo = 24

print(f'O JOGO DUROU {tempo} HORA(S)')