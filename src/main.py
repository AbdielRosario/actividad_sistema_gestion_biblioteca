from data.biblioteca import categorias, libros
from utils.operaciones import (
    agregar_categoria,
    buscar_por_paginas,
    contar_libros,
    mostrar_disponibles,
    promedio_paginas,
)

continuar = "s"

while continuar == "s":
    print("\n=== BIBLIOTECA ===")
    print("1. Ver libros disponibles")
    print("2. Buscar libros cortos (menos de 400 páginas)")
    print("3. Ver estadísticas")
    print("4. Agregar categoría")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        mostrar_disponibles(libros)
    elif opcion == "2":
        buscar_por_paginas(libros, 400)
    elif opcion == "3":
        print(f"Cantidad de libros: {contar_libros(libros)}")
        print(f"Promedio de páginas: {promedio_paginas(libros):.2f}")
    elif opcion == "4":
        nueva_categoria = input("Escribe la nueva categoría: ").strip()
        if not nueva_categoria:
            print("La categoría no puede estar vacía.")
        elif nueva_categoria in categorias:
            print("Esa categoría ya existe.")
        else:
            agregar_categoria(categorias, nueva_categoria)
            print(f'Categoría "{nueva_categoria}" agregada.')
            print(f"Categorías: {', '.join(sorted(categorias))}")
    elif opcion == "5":
        continuar = "n"
        print("¡Hasta pronto!")
    else:
        print("Opción no válida. Elige un número del 1 al 5.")
