def calcular_promedio(*args):
    resultado = 0

    for numero in args:
        resultado += numero

    resultado = resultado / len(args)

    return resultado

print( calcular_promedio(85,90,78,92) )