def calcular_fatorial(n, show=False):
    """
    -> Calcula el factorial de un número.
    :param n: O número a calcular.
    :param show: (Opcional) Mostrar o cálculo.
    :return: O valor do factorial de un número n.
    """
    if n == 0:
        return 1
    else:
        if show:
            if n == 1:
                print(n, end=' = ')
            else:
                print(n, end=' x ')
        return n * calcular_fatorial(n-1, show)


print(calcular_fatorial(5, True))
