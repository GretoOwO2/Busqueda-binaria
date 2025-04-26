import re

def iterative_binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def recursive_binary_search(arr, target, left, right):
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right)
    else:
        return recursive_binary_search(arr, target, left, mid - 1)

def main():
    print("Bienvenido a la búsqueda binaria interactiva!")
    print("¿Qué tipo de búsqueda deseas realizar?\n1. Iterativa\n2. Recursiva")
    opcion = input("Selecciona 1 o 2: ")

    numeros = input("Introduce una lista de números ordenados separados por espacios o comas: ")
    numeros_limpios = re.split(r'[ ,]+', numeros.strip())
    try:
        arr = list(map(int, numeros_limpios))
    except ValueError:
        print("Entrada inválida. Asegúrate de ingresar solo números separados por espacios o comas.")
        return

    try:
        target = int(input("¿Qué número deseas buscar?: "))
    except ValueError:
        print("Debes ingresar un número válido para buscar.")
        return

    if opcion == "1":
        resultado = iterative_binary_search(arr, target)
    elif opcion == "2":
        resultado = recursive_binary_search(arr, target, 0, len(arr) - 1)
    else:
        print("Opción no válida.")
        return

    if resultado != -1:
        print(f"✅ Elemento encontrado en el índice {resultado}.")
    else:
        print("❌ Elemento no encontrado.")

if __name__ == "__main__":
    main()
