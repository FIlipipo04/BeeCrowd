n = int(input())
while !=0:
    vet = lis(map(int, input().split()))
    vet.sort()
    pilha = [vet[0]]
    #pilha.ppend(vet[0])
    for i in range(1, len(vet)):
        if vet[i] in pilha:
            pilha.pop()
        else:
            pilha.append(vet[i])

    print(pilha[0])
    n = int(input())
