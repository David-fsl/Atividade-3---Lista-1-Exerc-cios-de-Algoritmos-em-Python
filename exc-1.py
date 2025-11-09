import time

def pesquisa_sequencial(lista, item):
    cont = 0
    for i, j in enumerate(lista):
        cont +=1
        if j == item:
            return i,cont
    return -1, cont   
lista = [1,2,3,4,5,6,7,8,9,10]
item = int(input("QUAL VALOR? "))
Resultado,cont = pesquisa_sequencial(lista,item)
print(Resultado)
print(cont)

# Medir o tempo de execução de um bloco de código
inicio = time.perf_counter()
for i in range(1000000):
    pass
fim = time.perf_counter()
print(f"Tempo de execução: {fim - inicio:.6f} segundos")