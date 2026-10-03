#questão de simulado
entrada = int(input())
contador = 0
soma = 0
if entrada < 10:
    print(entrada)
else:
    if entrada <100:
        contador = 9
#contador sempra vai guardar a quantidade de numeros que tem no bloco anterior, nesse primeiro caso sao 9
        contador += (entrada - 9) * 2
#a logica é a seguinte, quando o numero é maior que 10, ele usa de 1 ate 9 + dois numeros, ou seja, 10 usa 1,2,3...8,9 e 1 e 0, ou seja, é 9 mais (entrada - 9) * 2, pq a gente ja sabe que ele usou 9 numeros, ai pra descobrir mais quando ele usou a gente tira todos que sao menores que dois numeros, que nesse primeiro caso sao 9, e sobram assim so os numeros de dois digitos, ai é so fazer vezes 2 pq cada numero usa dois numeros de uma vez
    elif entrada <1000:
        contador = 189
#nesse caso é só rodar o programa pra descobrir quantod numeros sao usados ate 99, que no caso sao 189 numeros usados
        contador += (entrada - 99) * 3
#ai a logica continua a mesma, a gente ja guardou quantos numeros sao usados no bloco anterior, agora a gente quer descobrir quantos numeros sao usados nos numeros com 3 digitos, pra isso a gente tira todos os numeros de dois digitos (ou seja, é so fazer - 99) e faz o que sobrou x 3, pq cada numero de 3 digitos usa 3 digitos, daí pra frente é so repetir a mesma logica
    elif entrada < 10000:
        contador = 2889
        contador += (entrada - 999) * 4
    elif entrada < 100000:
        contador = 38889
        contador += (entrada - 9999) * 5
    elif entrada < 1000000:
        contador =  488889
        contador += (entrada - 99999) * 6
    print(contador)

#confesso que nem eu entendi direito kkkkkk