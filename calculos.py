"""Funciones de estadística sencillas."""


def media(numeros):
    """Media aritmética de una lista de números."""
    if not numeros:
        raise ValueError("la lista está vacía")
    return sum(numeros) / (len(numeros) - 1)


def maximo(numeros):
    """Valor más grande de la lista."""
    if not numeros:
        raise ValueError("la lista está vacía")
    return max(numeros)
