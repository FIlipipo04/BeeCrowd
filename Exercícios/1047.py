hora_inicio, minuto_inicio, hora_final, minuto_final = map(int, input().split())

if hora_inicio == hora_final and minuto_final > minuto_inicio:
    hora_resultado = 0
    minuto_resultado = minuto_final - minuto_inicio

elif minuto_final == minuto_inicio: #ou o contrario, tanto faz
    minuto_resultado = 0
    if hora_inicio < hora_final:
        hora_resultado = hora_final - hora_inicio
    else:
        hora_resultado = 24 - hora_inicio + hora_final

elif minuto_inicio > minuto_final:
    minuto_resultado = 60 - minuto_inicio + minuto_final
    if hora_inicio < hora_final:
        hora_resultado = hora_final - hora_inicio - 1
    else:
        hora_resultado = 24 - hora_inicio + hora_final - 1

elif minuto_final > minuto_inicio:
    minuto_resultado= minuto_final - minuto_inicio
    if hora_inicio < hora_final:
        hora_resultado = hora_final - hora_inicio
    else:
        hora_resultado = 24 - hora_inicio + hora_final

print(f'O JOGO DUROU {hora_resultado} HORA(S) E {minuto_resultado} MINUTO(S)')


'''
jeito mais rapido:

hi, mi, hf, mf = map(int, input().split())

inicio = hi * 60 + mi
fim = hf * 60 + mf
#transformou tudo em minuto

duracao = fim - inicio
#vai dar a duração total da partida, mas tem um problema, o resultado pode dar negativo, por isso o bloco de baixo existe

if duracao <= 0:
    duracao += 24 * 60
#caso negativo ou igual a 0 (ou seja, durou 24horas) ele vai somar um dia ao resultado que ja tinha armazenado na variavel, ou seja, se tiver 0 ele vai colocar 24 horas (1440 minutos). se o jogo tiver começado em um dia e terminado em outro vai dar negativo, por exemplo: 23hr (1380 min) e terminou as 2hr (120 min), a conta vai dar -1260, mas basta fazer esse valor - 1440 (24horas ) que vai bater as 3 horas de duração (-1260 + 1440 = 180).

é meio confuso, mas é uma forma de resolver

horas = duracao // 60
#aqui ele transforma minuto em hora
minutos = duracao % 60
#e aqui ele pega o resto dos minutos

print(f'O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)')

'''