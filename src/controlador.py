import os
from base_datos import BaseDatos

class GestorArticulos:
    def __init__(self):
        self.db = BaseDatos()
        self.indice_autor = {}
        self.indice_año = {}
        self.actualizar_indices()

    def actualizar_indices(self):
        self.indice_autor.clear()
        self.indice_año.clear()
        for nodo in self.db.tabla.tabla:
            while nodo:
                datos = nodo.valor
                autor = datos["autor"]
                año = datos["año"]
                clave = nodo.clave

                self.indice_autor.setdefault(autor, []).append(clave)
                self.indice_año.setdefault(año, []).append(clave)
                nodo = nodo.siguiente

    def agregar_articulo(self, clave, titulo, autor, año, archivo):
        if self.db.buscar(clave):
            print(f"[Aviso] Ya existe un artículo con la clave '{clave}'")
            return False
        self.db.agregar(clave, titulo, autor, año, archivo)
        self.actualizar_indices()
        return True

    def eliminar_articulo(self, clave):
        if self.db.eliminar(clave):
            self.actualizar_indices()
            return True
        print(f"[Error] No se encontró el artículo con clave '{clave}'")
        return False

    def buscar_por_clave(self, clave):
        return self.db.buscar(clave)

    def buscar_por_autor(self, autor):
        claves = self.indice_autor.get(autor, [])
        return [self.db.buscar(clave) for clave in claves]

    def buscar_por_año(self, año):
        claves = self.indice_año.get(año, [])
        return [self.db.buscar(clave) for clave in claves]

    def mostrar_todos(self):
        articulos = []
        for nodo in self.db.tabla.tabla:
            while nodo:
                articulos.append((nodo.clave, nodo.valor))
                nodo = nodo.siguiente
        return articulos
