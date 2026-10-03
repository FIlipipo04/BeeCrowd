qtd_repeticao = int(input()) #quantidade de repetiçoes 

for _ in range(0, qtd_repeticao):
    entrada = int(input()) #aqui vai pegar so os numeros que a gente quer testar
    soma = 0

    for c in range(1, (entrada //2 ) + 1): #aqui vai percorrer ate a metade mais 1 do numero, ja que nem um numero é divisivel por um numero maior que a sua metade
    
        if entrada % c == 0: 
            soma += c

    if soma == entrada:
        print(f'{entrada} eh perfeito')
    elif soma != entrada:
        print(f'{entrada} nao eh perfeito')
