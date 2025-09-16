from base_datos import BaseDatos
from articulo import Articulo
from manejo_archivos import ManejoArchivos


class GestorArticulos:
    def __init__(self):
        self.base_datos = BaseDatos()
        self.manejo_archivos = ManejoArchivos()

    def agregar_articulo(self, titulo, autores, año, ruta_archivo):
        try:
            # Leer contenido del archivo
            contenido = self.manejo_archivos.leer_archivo_texto(ruta_archivo)

            # Crear artículo
            articulo = Articulo(titulo, autores, año, contenido)

            # Guardar archivo con hash
            hash_archivo, ruta_guardada = self.manejo_archivos.guardar_archivo_con_hash(
                contenido
            )

            # Insertar en base de datos
            resultado = self.base_datos.insertar(articulo)
            return resultado

        except Exception as e:
            return f"Error al agregar artículo: {str(e)}"

    def buscar_articulo(self, hash_contenido):
        return self.base_datos.buscar(hash_contenido)

    def eliminar_articulo(self, hash_contenido):
        return self.base_datos.eliminar(hash_contenido)

    def actualizar_articulo(self, hash_contenido, titulo=None, autores=None, año=None):
        return self.base_datos.actualizar(hash_contenido, titulo, autores, año)

    def listar_todos_articulos(self):
        # Obtiene todos los artículos ordenados por título
        return self.base_datos.ordenar_por_titulo()

    def buscar_por_autor(self, autor):
        return self.base_datos.buscar_por_autor(autor)

    def buscar_por_año(self, año):
        return self.base_datos.buscar_por_año(año)

    def obtener_contenido_archivo(self, hash_contenido):
        articulo = self.base_datos.buscar(hash_contenido)
        if not articulo:
            return None

        try:
            ruta_archivo = f"data/archivos/{articulo.archivo}"
            return self.manejo_archivos.leer_archivo_texto(ruta_archivo)
        except Exception:
            return None
