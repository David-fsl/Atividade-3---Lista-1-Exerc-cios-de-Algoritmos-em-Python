
#  Qual a Complexidade da pesquisa sequencial?
#     A pesquisa sequencial tem a complexidade como O(n) porque o numero de tentativas é igual
#     o numero de elementos na lista.

#  Qual a complexidade da pesquisa binária?
#     A pesqueisa binaria a cada passo você divide pela metade, ou seja, o numero de passos
#     Cresce logaritmicamente com o tamanho da lista

import time

def pesquisa_sequencial(lista, item):
    cont = 0
    for i, j in enumerate(lista):
        cont += 1
        if j == item:
            return i, cont
    return -1, cont


def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
    cont = 0 

    while baixo <= alto:
        cont += 1 
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio, cont 
        if chute > item:
            alto = meio - 1 
        else:
            baixo = meio + 1 

    return -1, cont 

# lista = list(range(1,10000))
# lista = list(range(1,100000))
lista = list(range(1,1000000))
item1 = int(input('Qual o valor:'))

inicio = time.perf_counter()
resultado1,cont1 = pesquisa_sequencial(lista,item1)
print(resultado1)
print(cont1)
fim = time.perf_counter()
print(f"Tempo de execução: {fim - inicio:.6f} segundos")

inicio = time.perf_counter()
resultado2,cont2 = pesquisa_binaria(lista,item1)
print(resultado2)
print(cont2)
fim = time.perf_counter()
print(f"Tempo de execução: {fim - inicio:.6f} segundos")

