import os
from tabla_hash import TablaHashEncadenamiento
from articulo import Articulo
from manejo_archivos import ManejoArchivos


class BaseDatos:
    def __init__(self, archivo="data/articulos_db.txt"):
        self.tabla = TablaHashEncadenamiento()
        self.manejo = ManejoArchivos()
        self.archivo = archivo
        self.cargar_datos()

    def cargar_datos(self):
        if not os.path.exists(self.archivo):
            return

        with open(self.archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    articulo = Articulo.crear_desde_string_db(linea)
                    self.tabla.insertar(articulo.hash_contenido, articulo)
                except ValueError:
                    print(f"[Error] Línea inválida: {linea}")

    def existe(self, hash_contenido):
        return self.tabla.existe(hash_contenido)

    def guardar_en_archivo(self, articulo):
        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(articulo.convertir_a_string_db() + "\n")

    def insertar(self, articulo):
        if self.tabla.existe(articulo.hash_contenido):
            return "Artículo ya existe"

        self.tabla.insertar(articulo.hash_contenido, articulo)
        self.guardar_en_archivo(articulo)
        return "Artículo guardado"

    def buscar(self, hash_contenido):
        return self.tabla.buscar(hash_contenido)

    def reescribir_archivo(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for articulo in self.tabla.todos_valores():
                f.write(articulo.convertir_a_string_db() + "\n")

    def eliminar(self, hash_contenido):
        articulo = self.tabla.buscar(hash_contenido)
        if not articulo:
            return "Artículo no encontrado"

        self.tabla.eliminar(hash_contenido)
        self.manejo.eliminar_archivo_por_hash(hash_contenido)
        self.reescribir_archivo()

        return "Artículo eliminado"

    def actualizar(self, hash_contenido, titulo=None, autores=None, año=None):
        articulo = self.tabla.buscar(hash_contenido)
        if not articulo:
            return "Artículo no encontrado"

        if titulo:
            articulo.titulo = titulo
        if autores:
            articulo.autores = autores
        if año:
            articulo.año = int(año)

        self.reescribir_archivo()
        return "Artículo actualizado"

    def todos_articulos(self):
        return self.tabla.todos_valores()

    def buscar_por_autor(self, autor):
        resultado = []
        for articulo in self.tabla.todos_valores():
            if autor.lower() in articulo.autores.lower():
                resultado.append(articulo)
        return sorted(resultado, key=lambda a: a.autores.lower())

    def buscar_por_año(self, año):
        resultado = []
        for articulo in self.tabla.todos_valores():
            if articulo.año == año:
                resultado.append(articulo)
        return sorted(resultado, key=lambda a: a.titulo.lower())

    def ordenar_por_titulo(self):
        return sorted(self.tabla.todos_valores(), key=lambda a: a.titulo.lower())

    def ordenar_por_autor(self):
        return sorted(self.tabla.todos_valores(), key=lambda a: a.autores.lower())
