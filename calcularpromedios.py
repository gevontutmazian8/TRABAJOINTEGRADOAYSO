lista = []

for i in range(3):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {i + 1} (entre 0 y 10): "))
            if 0 <= nota <= 10:
                lista.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10. Inténtalo de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número.")


def calcular_promedio(notas):
    if len(notas) == 0:
        return 0
    return sum(notas) / len(notas)

print("El promedio de las notas es:", calcular_promedio(lista))