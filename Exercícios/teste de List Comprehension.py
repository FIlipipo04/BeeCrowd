# pares = [par for par in range(1, 100) if par % 2 == 0]
# impares = [imp for imp in range(1, 100) if imp % 2!= 0]
# print('Esses são os numeros pares: \n', *pares)
# print('\nEsses são os numeros impares: \n', *impares)

# letras = ['a', 'b', 'c']
# numeros = [1, 2, 3]
# com = [(l, n) for l in letras for n in numeros]
# print(*com)

# quando se trata de matrizes, vamos ter dois colchetes 
# mat = [[j+1+i*4 for j in range(4)]for i in range(3)]
# print(mat)

# transposta = [[linha[i] for linha in mat]for i in range(4)]
# print(transposta)

# f =['banana     ', '      abacate ', '   anana              ']
# f2 = [f.strip().upper() for f in f]
# print(f2)

# frase = 'Exemplo de list-comprehension com set'
# vogais_todas = [c for c in frase if c in 'aeiouAEIOU']
# vogais_unicas = {c for c in frase if c in 'aeiouAEIOU'}
# print(vogais_todas)
# print(vogais_unicas)

# q = {f'{i}':i**3 for i in range(2, 10)}
# print(q)

num = [1, 2, 3, 4, 5]
ger = (x**2 for x in num)
print(ger)
for item in ger:
    print(item)

# testar os outros exemplos do slide 14
