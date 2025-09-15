from controlador import GestorArticulos

def mostrar_articulo(clave, datos):
    print(f"Clave: {clave}")
    print(f"  Título: {datos['titulo']}")
    print(f"  Autor: {datos['autor']}")
    print(f"  Año: {datos['año']}")
    print(f"  Archivo: {datos['archivo']}")
    print("-" * 40)

def menu():
    gestor = GestorArticulos()

    while True:
        print("\n--- Menú de Gestión de Artículos ---")
        print("1. Agregar artículo")
        print("2. Eliminar artículo")
        print("3. Buscar por clave")
        print("4. Buscar por autor")
        print("5. Buscar por año")
        print("6. Mostrar todos")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            clave = input("Clave: ")
            titulo = input("Título: ")
            autor = input("Autor: ")
            año = input("Año: ")
            archivo = input("Archivo: ")
            gestor.agregar_articulo(clave, titulo, autor, año, archivo)

        elif opcion == "2":
            clave = input("Clave a eliminar: ")
            gestor.eliminar_articulo(clave)

        elif opcion == "3":
            clave = input("Clave a buscar: ")
            datos = gestor.buscar_por_clave(clave)
            if datos:
                mostrar_articulo(clave, datos)
            else:
                print("Artículo no encontrado.")

        elif opcion == "4":
            autor = input("Autor a buscar: ")
            resultados = gestor.buscar_por_autor(autor)
            for datos in resultados:
                mostrar_articulo(datos["titulo"], datos)

        elif opcion == "5":
            año = input("Año a buscar: ")
            resultados = gestor.buscar_por_año(año)
            for datos in resultados:
                mostrar_articulo(datos["titulo"], datos)

        elif opcion == "6":
            todos = gestor.mostrar_todos()
            for clave, datos in todos:
                mostrar_articulo(clave, datos)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")

menu()