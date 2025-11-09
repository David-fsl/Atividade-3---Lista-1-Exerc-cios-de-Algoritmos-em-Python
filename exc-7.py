import random
import time
from typing import List, Tuple

def selection_sort(a: List[int]) -> List[int]:
    a = a[:]  # trabalha em cópia
    n = len(a)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


def quicksort(a: List[int]) -> List[int]:
    if len(a) <= 1:
        return a
    pivot = a[len(a)//2]  # pivô do meio para reduzir chance do pior caso
    menores = [x for x in a if x < pivot]
    iguais  = [x for x in a if x == pivot]
    maiores = [x for x in a if x > pivot]
    return quicksort(menores) + iguais + quicksort(maiores)


#_________________________________________________________

def busca_sequencial(a: List[int], alvo: int) -> Tuple[int, int]:
    comps = 0
    for i, v in enumerate(a):
        comps += 1  # compara v == alvo
        if v == alvo:
            return i, comps
    return -1, comps


def busca_binaria(a: List[int], alvo: int) -> Tuple[int, int]:
    lo, hi = 0, len(a) - 1
    comps = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comps += 1  # a[mid] == alvo
        if a[mid] == alvo:
            return mid, comps
        comps += 1  # a[mid] < alvo
        if a[mid] < alvo:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comps
# ___________________________________________

def main():
    # 1) Geração dos dados
    random.seed(42)  # reprodutibilidade
    N = 1000
    dados = [random.randint(1, 10_000) for _ in range(N)]

    resultados = []

    # 2) Ordenação por seleção
    t0 = time.perf_counter()
    ord_sel = selection_sort(dados)
    t_sel = (time.perf_counter() - t0) * 1000  # em ms
    resultados.append(("Selection Sort", t_sel, ord_sel == sorted(dados)))

    # 3) Quicksort recursivo
    t0 = time.perf_counter()
    ord_qs = quicksort(dados)
    t_qs = (time.perf_counter() - t0) * 1000
    resultados.append(("Quicksort (rec)", t_qs, ord_qs == sorted(dados)))

    # 4) Função built-in sorted() (Timsort)
    t0 = time.perf_counter()
    ord_builtin = sorted(dados)
    t_builtin = (time.perf_counter() - t0) * 1000
    resultados.append(("sorted() (Timsort)", t_builtin, True))

    # Verificação de consistência
    assert ord_sel == ord_qs == ord_builtin

    # 5) Tabela de tempos
    header = f"{'Método':<20} {'Tempo (ms)':>12} {'Correto?':>10}"
    print(header)
    print('-' * len(header))
    for nome, tempo, ok in resultados:
        print(f"{nome:<20} {tempo:12.3f} {str(ok):>10}")

    # 6) Busca com valor digitado pelo usuário
    while True:
        try:
            alvo = int(input("\nDigite um valor inteiro para buscar (1 a 10000): "))
            if 1 <= alvo <= 10_000:
                break
            print("Por favor, digite um número entre 1 e 10000.")
        except ValueError:
            print("Entrada inválida. Tente novamente com um número inteiro.")

    # Pesquisar na lista já ORDENADA (usaremos a ord_builtin)
    idx_seq, comps_seq = busca_sequencial(ord_builtin, alvo)
    idx_bin, comps_bin = busca_binaria(ord_builtin, alvo)

    # 7) Resultado das buscas
    def fmt_result(idx: int) -> str:
        return f"encontrado no índice {idx}" if idx != -1 else "NÃO encontrado"

    print("\nResultados da busca:")
    print(f"- Sequencial: {fmt_result(idx_seq)} | Comparações: {comps_seq}")
    print(f"- Binária:    {fmt_result(idx_bin)} | Comparações: {comps_bin}")

    # Observação útil
    print("\nObs.: A busca binária é O(log n) e tende a usar ~log2(n) passos;")
    print("já a busca sequencial é O(n) e, em média, percorre metade da lista quando o valor existe.")


if __name__ == "__main__":
    main()