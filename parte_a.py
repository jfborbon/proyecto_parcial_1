"""
Por: Juan Felipe Borbón Melo
Fecha: 9/03/2025
Matemáticas Discretas y sus Aplicaciones
2025-1

"""

# Parte A

v = dict()

def str_a_list(string: str, ignore: set) -> list:
    cars = []
    for atomo in string:
        if atomo not in ignore:
            cars.append(atomo)
    return cars

def valoracion(formula, der: int, izq: int):
    resultado = -1
    if der == izq:
        if formula[der] in v:
            resultado = v[formula[der]]
    elif formula[der] == '!':
        resultado = 1 - valoracion(formula, der + 1, izq)
    elif formula[der] == '(' and formula[izq] == ')':
        count, i, oper = 0, der + 1, -1
        while i < izq and oper == -1:
            if formula[i] == '(':
                count += 1
            elif formula[i] == ')':
                count -= 1
            if formula[i] in {'&', '|'} and count == 0:
                oper = i
            i += 1
        
        if oper != -1:
            izquierda = valoracion(formula, der + 1, oper - 1)
            derecha = valoracion(formula, oper + 1, izq - 1)
            if izquierda != -1 and derecha != -1:
                if formula[oper] == '&':
                    resultado = izquierda and derecha
                elif formula[oper] == '|':
                    resultado = izquierda or derecha
        else:
            resultado = -1
    return resultado

def main_a():
    print("Parte A\n")
    N = int(input())
    if 1 <= N <= 5:
        for j in range(N):
            entrada = input().split()
            if len(entrada) == 2 and entrada[1] in {'0', '1'}:
                v[entrada[0]] = int(entrada[1])
            else:
                print("Valor inválido")
    else:
        print("Fuera de rango (1 - 5)")
        
    S = int(input())
    if 1 <= S <= 100:    
        for k in range(S):
            formula = str_a_list(input(), {' '})
            resultado = valoracion(formula, 0, len(formula) - 1)
            print("-1" if resultado == -1 else "1" if resultado else "0")
    else:
        print("Fuera de rango (1 - 100)")

main_a()