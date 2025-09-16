import sys
import os

# Agregar el directorio src al path para importaciones
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from interfaz_grafica import InterfazGrafica


def main():
    try:
        print("Iniciando Gestor de Artículos Científicos...")

        # Crear e iniciar la interfaz gráfica
        app = InterfazGrafica()
        app.ejecutar()

    except Exception as e:
        print(f"Error al iniciar la aplicación: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
