entrada = int(input())

ano = (entrada // 365)
mes = (entrada % 365) // 30 
dias = ((entrada % 365) % 30)

print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dias} dia(s)')