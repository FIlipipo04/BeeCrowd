import time
def loop(n): #Função usando loop iterativo
result = []
for i in range(n):
if i % 2 == 0:
result.append(i*i)
return result
def listc(n): #Função usando list-comprehension
return [i*i for i in range(n) if i % 2 == 0]
#print(time.asctime(time.localtime(inicio)))
inicio = time.time() #captura do tempo inicial
loop(10**7)
fim = time.time() #captura do tempo final
print('Tempo com loop iterativo:', round(fim - inicio, 2))
inicio = time.time() #captura do tempo inicial
listc(10**7)
fim = time.time() #captura do tempo final
print('Tempo com list-comprehension', round(fim - inicio, 2))