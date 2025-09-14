import os
from tabla_hash import TablaHashEncadenamiento

class BaseDatos:
    def __init__(self, archivo="articulos_db.txt"):
        self.archivo = archivo
        self.tabla = TablaHashEncadenamiento()
        self.cargar_datos()

    def cargar_datos(self):
        if not os.path.exists(self.archivo):
            open(self.archivo, "w").close()
            return

        with open(self.archivo, "r", encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue
                try:
                    clave, titulo, autor, año, archivo = linea.split("|")
                    self.tabla.insertar(clave, {
                        "titulo": titulo,
                        "autor": autor,
                        "año": año,
                        "archivo": archivo
                    })
                except ValueError:
                    print(f"[Error] Línea inválida: {linea}")

    def sincronizar(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for indice in self.tabla.tabla:
                nodo = indice
                while nodo:
                    clave = nodo.clave
                    datos = nodo.valor
                    f.write(f"{clave}|{datos['titulo']}|{datos['autor']}|{datos['año']}|{datos['archivo']}\n")
                    nodo = nodo.siguiente

    def agregar(self, clave, titulo, autor, año, archivo):
        self.tabla.insertar(clave, {
            "titulo": titulo,
            "autor": autor,
            "año": año,
            "archivo": archivo
        })
        self.sincronizar()

    def buscar(self, clave):
        return self.tabla.buscar(clave)

    def eliminar(self, clave):
        if self.tabla.eliminar(clave):
            self.sincronizar()
            return True
        return False
