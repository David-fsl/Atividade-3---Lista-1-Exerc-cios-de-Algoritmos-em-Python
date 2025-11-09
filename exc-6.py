import random
import time

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista)//2]
    menores = [x for x in lista if x < pivot]
    iguais  = [x for x in lista if x == pivot]
    maiores = [x for x in lista if x > pivot]
    return quicksort(menores) + iguais + quicksort(maiores)


def selecao_sort(lista):
    a = lista[:]  # não altera a original
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a
# _________________________________________
if __name__ == "__main__":
    # Gera uma lista aleatória de 10.000 inteiros
    random.seed(42)
    N = 10_000
    lista = [random.randint(0, 1_000_000) for _ in range(N)]

    # Quicksort
    t0 = time.perf_counter()
    qs_sorted = quicksort(lista)
    t_qs = time.perf_counter() - t0
    assert qs_sorted == sorted(lista)

    # Selection Sort (pode ser bem mais lento)
    t0 = time.perf_counter()
    ss_sorted = selecao_sort(lista)
    t_ss = time.perf_counter() - t0
    assert ss_sorted == sorted(lista)

    print(f"Tempo quicksort:     {t_qs:.6f} s")
    print(f"Tempo seleção sort:  {t_ss:.6f} s")