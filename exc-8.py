import random
from typing import List

# -------------- Funções Recursivas --------------

def soma_recursiva(lista: List[int], i: int = 0) -> int:
    """Soma acumulada recursiva dos elementos da lista."""
    if i == len(lista):
        return 0
    return lista[i] + soma_recursiva(lista, i + 1)

def quicksort(lista: List[int]) -> List[int]:
    """Quicksort recursivo (versão funcional)."""
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista)//2]  # pivô do meio
    menores = [x for x in lista if x < pivot]
    iguais  = [x for x in lista if x == pivot]
    maiores = [x for x in lista if x > pivot]
    return quicksort(menores) + iguais + quicksort(maiores)

def busca_binaria_rec(lista: List[int], alvo: int, ini: int, fim: int) -> int:
    """Busca binária recursiva. Retorna índice ou -1."""
    if ini > fim:
        return -1
    meio = (ini + fim) // 2
    if lista[meio] == alvo:
        return meio
    if lista[meio] < alvo:
        return busca_binaria_rec(lista, alvo, meio + 1, fim)
    else:
        return busca_binaria_rec(lista, alvo, ini, meio - 1)

def fatorial(n: int) -> int:
    """Fatorial recursivo."""
    if n < 0:
        raise ValueError("fatorial não definido para n negativo")
    if n <= 1:
        return 1
    return n * fatorial(n - 1)

def fibonacci(n: int) -> int:
    """Fibonacci recursivo simples. F(0)=0, F(1)=1."""
    if n < 0:
        raise ValueError("fibonacci não definido para n negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# -------------- Programa Principal --------------

def main():
    random.seed(42)   # reprodutível
    N = 20
    # Inclui 100 no intervalo para a checagem fazer sentido
    lista = [random.randint(1, 120) for _ in range(N)]

    # Soma recursiva
    soma_total = soma_recursiva(lista)

    # Ordenação com quicksort
    ordenada = quicksort(lista)

    # Busca binária recursiva por 100
    idx_100 = busca_binaria_rec(ordenada, 100, 0, len(ordenada) - 1)
    contem_100 = (idx_100 != -1)

    # Fatorial do maior número
    maior = max(lista)
    fat_maior = fatorial(maior)
    num_digitos_fat = len(str(fat_maior))

    # Fibonacci de n, onde n = tamanho da lista
    fib_n = fibonacci(len(lista))

    # Saída
    print("Lista original (20 números):")
    print(lista)
    print("\nSoma recursiva dos elementos:", soma_total)

    print("\nLista ordenada (quicksort):")
    print(ordenada)

    print("\nBusca binária recursiva por 100:")
    if contem_100:
        print(f"-> 100 ENCONTRADO no índice {idx_100} da lista ordenada.")
    else:
        print("-> 100 NÃO encontrado.")

    print(f"\nMaior elemento da lista: {maior}")
    print(f"Fatorial({maior}) tem {num_digitos_fat} dígitos.")

    print(f"\nFibonacci(n) com n = tamanho da lista ({N}): {fib_n}")

if __name__ == "__main__":
    main()