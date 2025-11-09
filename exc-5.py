def fatorial(n: int) -> int:
    if n < 0:
        raise ValueError("fatorial não está definido para n negativo")
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("fibonacci não está definido para n negativo")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def soma_acumulada(n: int) -> int:
 
    if n < 0:
        raise ValueError("soma_acumulada não está definida para n negativo")
    if n == 0:
        return 0
    return n + soma_acumulada(n - 1)
# _________________________________________
if __name__ == "__main__":
    # fatorial para 0 a 6
    print("Fatorial:")
    for i in range(0, 7):
        print(f"{i}! = {fatorial(i)}")

    # fibonacci para n = 0, 1, 5, 10
    print("\nFibonacci:")
    for n in [0, 1, 5, 10]:
        print(f"F({n}) = {fibonacci(n)}")

    # soma_acumulada para n = 10
    print("\nSoma acumulada até 10:")
    print(f"soma_acumulada(10) = {soma_acumulada(10)}")