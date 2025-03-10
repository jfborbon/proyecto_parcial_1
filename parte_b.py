"""
Por: Juan Felipe Borbón Melo
Fecha: 9/03/2025
Matemáticas Discretas y sus Aplicaciones
2025-1

"""

# Parte B

from parte_a import str_a_list, valoracion, v

def extraer_atomos(expresion):
    atomos = []
    operadores = {'(', ')', '!', '&', '|'}
    for i in expresion:
        if i not in operadores and i not in atomos:
            atomos.append(i)
    return atomos
 

def generar_valores(atomos):
    n_atomos = len(atomos)  
    total_combinaciones = 2 ** n_atomos  
    combinaciones = []

    for i in range(total_combinaciones):
        combinacion = {}
        num = i
        valores_binarios = [0] * n_atomos

        for j in range(n_atomos - 1, -1, -1):  
            valores_binarios[j] = num % 2
            num = num // 2

        for k in range(n_atomos):
            combinacion[atomos[k]] = valores_binarios[k]

        combinaciones.append(combinacion)

    return combinaciones

def evaluador(formula):
    form = str_a_list(formula, {' '})
    atomos = extraer_atomos(form)
    valoraciones = generar_valores(atomos)
    resultados = set()
    
    for asignacion in valoraciones:
        v.update(asignacion)
        resultado = valoracion(form, 0, len(form) - 1)
        if resultado == -1:
            return -1
        resultados.add(resultado)
    
    return 1 if len(resultados) == 1 and 1 in resultados else 0 if len(resultados) == 1 else -1

def main_b():
    print("\nParte B\n")
    S = int(input())
    if 1 <= S <= 20:
        for l in range(S):
            formula = str(input())
            if len(formula) <= 32:
                print(evaluador(formula))
            else:
                print("Fórmula excede 32 caracteres")
    else:
        print("Fuera de rango (1 - 20)")

main_b()
